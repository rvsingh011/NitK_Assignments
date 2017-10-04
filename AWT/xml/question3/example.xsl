<?xml version="1.0" encoding="UTF-8"?>
<html xsl:version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format">
    <body>
        <head>
            <link rel="stylesheet" type="text/css" href="bootstrap.css" />
        </head>
        <div class="jumbotron">
            <xsl:for-each select="ads/add[1]">
                <h3>Musical show</h3>
                <h3>Performed By:</h3>
                <h1>
                    <xsl:value-of select="band/node()"/>
                </h1>
                <h3>on</h3>
                <h1>
                    <xsl:value-of select="date/node()"/>
                </h1>
                <h3>at</h3>
                <h1>
                    <xsl:value-of select="location/node()"/>
                </h1>
            </xsl:for-each>
        </div>

    </body>
</html>
