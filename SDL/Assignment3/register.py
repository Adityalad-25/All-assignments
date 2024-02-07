from lxml import etree

# Load the XML Schema

schema_file = 'SDL\\Assignment3\\register_schema.xsd'

schema = etree.XMLSchema(etree.parse(schema_file))


# Load the XML document

xml_file = 'SDL\\Assignment3\\register.xml'

xml_doc = etree.parse(xml_file)


# Validate the XML document against the schema

if schema.validate(xml_doc):

    print("Validation successful.")

else:

    print("Validation failed. Errors:")

    for error in schema.error_log:

        print(error)