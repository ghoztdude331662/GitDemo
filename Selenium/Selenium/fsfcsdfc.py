from graphviz import Digraph

# Create a new directed graph
diagram = Digraph("UML Class Diagram", format="png")

# Define Customer class
diagram.node(
    "Customer",
    """Customer
------------------------
+ CustomerID: int
+ CustomerName: string
+ CustomerType: string
+ DateOfFinding: date
------------------------
+ addCustomer(): void
+ editCustomer(): void
+ searchCustomer(): void""",
    shape="record"
)

# Define CustomerDetails class
diagram.node(
    "CustomerDetails",
    """CustomerDetails
------------------------
+ Address_1: string
+ Address_2: string
+ City: string
+ PostalCode: string
+ Phone: string
+ Fax: string
+ Website: string
+ Location: string[]
------------------------
+ addLocation(): void
+ updateLocation(): void""",
    shape="record"
)

# Define the relationship between Customer and CustomerDetails
diagram.edge("Customer", "CustomerDetails", label="1..*", arrowhead="crow")

# Save and render the UML class diagram
diagram.render("uml_class_diagram_sample", cleanup=True)

print("UML class diagram created as uml_class_diagram_sample.png")
