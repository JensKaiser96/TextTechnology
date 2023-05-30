class XPathHelper:
    """
    Helper Class to build XPath Expressions for scrapy.
    Example with `response` Object from scrapy, first the normal way, and then using XPathHelper

    >>> date = response.xpath("./div[contains(concat(' ',@class,' '),' Class1 ')]//a/@date").get()
    >>> date = XPathHelper.root(response).div("Class1").skip.a().attribute("date").get()

    This Class helps to avoid spelling mistakes and the cumbersome class selection in the cases where 
    the target node has multiple classes but we only want to have on of those classes in the selector
    definition.

    It is still possible and very easy to build invalid or wrong path descriptors.
    """

    # set to True to enable printing out the path when building
    enable_print_path = False

    # Constructors
    def __init__(self, selector, path=""):
        self.selector = selector
        if path:
            self.path = path

    @staticmethod
    def root(selector):
        return XPathHelper(selector, path="")

    @staticmethod
    def desc(selector):
        return XPathHelper(selector, path="/")

    @staticmethod
    def rel_desc(selector):
        return XPathHelper(selector, path="./")

    # Builders
    def build(self):
        if self.enable_print_path:
            print(f"\n * XPath='{self.path}'")
        return self.selector.xpath(self.path)

    def get(self):
        return self.build().get()

    def getall(self):
        return self.build().getall()

    def bool(self):
        return bool(self.getall)

    # Content Selectors
    def text(self):
        self.path += "/text()"
        return self

    # Nodes
    def node(self, node_name="*", _class_=""):
        self.path += f"/{node_name}"
        if _class_:
            self._class_(_class_)
        return self

    @property
    def skip(self):
        self.path += "/"
        return self

    def div(self, _class_=""):
        return self.node("div", _class_)

    def a(self, _class_=""):
        return self.node("a", _class_)

    def decenedent(self, node_name="*", _class_=" "):
        return self.skip.node(node_name. _class_)

    # attributes
    def _class_(self, class_name):
        self.path += f"[contains(concat(' ',@class,' '),' {class_name} ')]"
        return self

    def attribute(self, attribte_name):
        self.path += f"/@{attribte_name}"
        return self

    def href(self):
        return self.attribute("href")
