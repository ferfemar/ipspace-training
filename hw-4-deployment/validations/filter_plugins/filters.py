#!/usr/bin/python
class FilterModule(object):
    def filters(self):
        return {
            'is_list': self.is_list,
            # 'rekey_junos_interfaces': self.rekey_junos_interfaces,
            'normalize_xml': self.normalize_xml,
            'parse_junos_interfaces': self.parse_junos_interfaces,
            'parse_cisco_interfaces': self.parse_cisco_interfaces
        }

    def is_list(self, value):
        return isinstance(value, list)

    # def rekey_junos_interfaces(self, interfaces_xml):
    #     import jxmlease
    #     interfaces_dict = jxmlease.parse(interfaces_xml)
    #     for interface in interfaces_dict['configuration']['interfaces']['interface']:
    #         interface['unit'].jdict(in_place=True)
    #     interfaces_dict['configuration']['interfaces']['interface'].jdict(
    #         in_place=True)
    #     return interfaces_dict

    def normalize_xml(self, xml_string):
        """ Takes XML document as string and strips whitespaces.
        Returnes the normalized XML document as string.
        """
        from lxml import etree
        normalize_xslt = etree.XML('''\
        <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
            <xsl:output method="xml" indent="no"/>
            <xsl:template match="/*[local-name()='rpc-reply']/*[local-name()='output']">
                <xsl:copy-of select="."/>
            </xsl:template>
            <xsl:template match="/|comment()|processing-instruction()">
                <xsl:copy>
                    <xsl:apply-templates/>
                </xsl:copy>
            </xsl:template>
            <xsl:template match="*">
                <xsl:element name="{local-name()}">
                    <xsl:apply-templates select="@*|node()"/>
                </xsl:element>
            </xsl:template>
            <xsl:template match="@*">
                <xsl:attribute name="{local-name()}">
                    <xsl:value-of select="."/>
                </xsl:attribute>
            </xsl:template>
            <xsl:template match="text()">
                <xsl:value-of select="normalize-space(.)"/>
            </xsl:template>
        </xsl:stylesheet>''')
        transform = etree.XSLT(normalize_xslt)
        xml = etree.fromstring(xml_string)
        result = transform(xml)
        return str(result)

    def parse_junos_interfaces(self, interfaces_xml):
        """Transform Juniper XML interfaces configuration blob 
        into a YAML file for interface.unit lookups
        """
        from lxml import etree
        template = etree.XML("""
        <xsl:stylesheet version="1.0"
                        xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

        <xsl:output method="text" encoding="utf-8"/>

        <xsl:template match="/">
        <xsl:for-each select="configuration/interfaces/interface">
        <xsl:for-each select="unit">
        <xsl:value-of select="../name"/>.<xsl:value-of select="name"/>:
        address: <xsl:value-of select="family/inet/address"/>
        <xsl:text>&#xa;</xsl:text>
        </xsl:for-each>
        </xsl:for-each>
            
        </xsl:template>
        </xsl:stylesheet>
        """)

        transform = etree.XSLT(template)
        interfaces = etree.fromstring(interfaces_xml)
        result = transform(interfaces)
        return str(result)

    def parse_cisco_interfaces(self, interfaces_list):
        """Transform Cisco configuration blob (interfaces)
        into a YAML file for interface.unit lookups
        """
        from netaddr import IPAddress
        interfaces_dict = {interface['name']: interface for interface in interfaces_list}
        for interface in interfaces_dict:
            prefixlen = ""
            if interfaces_dict[interface].get('mask'):
                prefixlen = IPAddress(
                    interfaces_dict[interface].get('mask')).netmask_bits()
                interfaces_dict[interface]['address'] = "{}/{}".format(
                    interfaces_dict[interface].get('address'), prefixlen)
            interfaces_dict[interface].pop('mask')
            interfaces_dict[interface].pop('name')

        return interfaces_dict
