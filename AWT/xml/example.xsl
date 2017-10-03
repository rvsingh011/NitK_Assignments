<?xml version="1.0" encoding="UTF-8"?>
<html xsl:version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<body style="font-family:Arial;font-size:12pt;background-color:#EEEEEE">
  <head>
    <style>
      table, th, td {
         border: 1px solid black;
      }
    </style>
  </head>
<table>
  <tr>
    <td>

  </tr>
<xsl:for-each  select="/ads/add">
    
    <xsl:value-of select="price"/>
</xsl:for-each>
</body>
</html>
