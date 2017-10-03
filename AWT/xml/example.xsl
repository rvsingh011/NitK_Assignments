<?xml version="1.0" encoding="UTF-8"?>
<html xsl:version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format">
    <body>
        <head>
            <style>
                table,
                td,
                th {
                    border: 1px solid black;
                }

            </style>
        </head>
        <table>
            <tr>

                <xsl:for-each select="ads/add[1]/*">
                    <td>
                        <xsl:value-of select="local-name()"/>
                    </td>
                </xsl:for-each>
            </tr>

            <xsl:for-each select="ads/*">
                <tr>

                    <xsl:for-each select="./*">

                        <xsl:if test="not(*)">

                            <xsl:if test="name() = 'genre'">

                                <xsl:variable name="mygen">

                                    <xsl:value-of select="node()"/>
                                    <!-- mygen = pop-->
                                </xsl:variable>

                                <xsl:if test="$mygen='Rock'">
                                    <td bgcolor="green"><xsl:value-of select="node()"/></td>
                                </xsl:if>

                                <xsl:if test="$mygen='classical'">
                                    <td bgcolor="yellow"><xsl:value-of select="node()"/></td>
                                </xsl:if>

                                <xsl:if test="$mygen='instrumental'">
                                    <td bgcolor="blue"><xsl:value-of select="node()"/></td>
                                </xsl:if>

                            </xsl:if>

                            <xsl:if test="not(name() = 'genre')">
                                <td>
                                    <xsl:value-of select="node()"/>
                                </td>
                            </xsl:if>
                        </xsl:if>

                        <xsl:if test="./*">
                            <td>

                                <xsl:for-each select="*">

                                    <xsl:if test="not(*)">

                                        <xsl:value-of select="local-name()"/>:

                                        <xsl:value-of select="node()"/><br/>
                                    </xsl:if>

                                    <xsl:for-each select="*">

                                        <xsl:value-of select="local-name()"/>:

                                        <xsl:value-of select="node()"/><br/>
                                    </xsl:for-each>
                                </xsl:for-each>
                            </td>
                        </xsl:if>
                        <!-- <xsl:if test="./*">
                                <xsl:for-each select="./*">
                                    <xsl:value-of select="node()"/>
                                </xsl:for-each>
                            </xsl:if> -->

                    </xsl:for-each>
                </tr>
            </xsl:for-each>
        </table>

        <!-- <xsl:for-each select="ads/add/*">
       <xsl:value-of select ="local-name()"/>
   </xsl:for-each> -->

        <!-- <xsl:for-each  select="/ads/add">

    <xsl:value-of select="price"/>
</xsl:for-each> -->
    </body>
</html>
