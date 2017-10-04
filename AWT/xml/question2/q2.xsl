<?xml version="1.0" encoding="UTF-8"?>
<html xsl:version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format">

    <body>
        <table border="1" style="width:100%">

          <tr bgcolor="">
            <th rowspan="3" >Name</th>
            <th rowspan="3" >Genre</th>
            <th colspan="3" >Performers</th>
            <th rowspan="3" >Date</th>
            <th rowspan="3" >Time</th>
            <th colspan="6" >Place</th>
            <th rowspan="3" >Ticket</th>
            <th colspan="4" >SellerInfo</th>
          </tr>
          <tr>
            <th rowspan="2">FirstName</th>
            <th rowspan="2">LastName</th>
            <th rowspan="2">Role</th>
            <th rowspan="2">Venue</th>
            <th colspan="4">address</th>
            <th rowspan="2">Contact</th>
            <th rowspan="2">Name</th>
            <th rowspan="2">Email</th>
            <th rowspan="2">Phone</th>
            <th rowspan="2">address</th>
          </tr>
          <tr>
            <th>City</th>
            <th>Street</th>
            <th>District</th>
            <th>State</th>
          </tr>

          <xsl:for-each select="concerts/concert">
            <xsl:sort select="name"/>

          <tr>

            <xsl:variable name = "mytgold">
              <xsl:value-of select = "ticket/gold"/>
            </xsl:variable>
            <xsl:variable name = "mytsilver">
              <xsl:value-of select = "ticket/silver"/>
            </xsl:variable>
            <xsl:variable name = "mytord">
              <xsl:value-of select = "ticket/ordinary"/>
            </xsl:variable>
            <xsl:variable name = "mystate">
              <xsl:value-of select = "place/adress/state"/>
            </xsl:variable>
            <xsl:variable name = "mymonth">
              <xsl:value-of select = "date/month"/>
            </xsl:variable>

            <xsl:if test="($mytgold &lt;= 100) or ($mytsilver &lt;= 100) or ($mytord &lt;= 100)">
               <xsl:if test="$mystate='Karnataka'">
                 <xsl:if test="$mymonth='April'">

                      <td><xsl:value-of select="name"/></td>
                          <xsl:variable name = "mygen">
                        <xsl:value-of select = "genre"/> <!-- mygen = pop-->
                      </xsl:variable>

                      <xsl:if test="$mygen='pop'">
                         <td bgcolor="green" ><xsl:value-of select="genre"/></td>
                      </xsl:if>
                      <xsl:if test="$mygen='classical'">
                         <td bgcolor="yellow" ><xsl:value-of select="genre"/></td>
                      </xsl:if>
                      <xsl:if test="$mygen='instrumental'">
                         <td bgcolor="blue" ><xsl:value-of select="genre"/></td>
                      </xsl:if> 
                      <td><xsl:value-of select="performers/performer/firstname"/></td>
                      <td><xsl:value-of select="performers/performer/lastname"/></td>
                      <td><xsl:value-of select="performers/performer/role"/></td>
                      <td>
                        <xsl:value-of select="date/month"/>
                        <xsl:value-of select="date/day"/>
                        <xsl:value-of select="date/year"/>
                      </td>
                      <td><xsl:value-of select="time"/></td>
                      <td><xsl:value-of select="place/venue"/></td>
                      <td><xsl:value-of select="place/adress/city"/></td>
                      <td><xsl:value-of select="place/adress/street"/></td>
                      <td><xsl:value-of select="place/adress/district"/></td>
                      <td><xsl:value-of select="place/adress/state"/></td>
                      <td><xsl:value-of select="place/contact"/></td>
                      <xsl:if test="$mytgold &lt; 100">
                        <td>gold-<xsl:value-of select="ticket/gold"/></td>
                      </xsl:if>
                      <xsl:if test="$mytsilver &lt; 100">
                        <td>silver-<xsl:value-of select="ticket/silver"/></td>
                      </xsl:if>
                      <xsl:if test="$mytord &lt; 100">
                        <td>ordinary-<xsl:value-of select="ticket/ordinary"/></td>
                      </xsl:if>
                      <td><xsl:value-of select="sellerinfo/name"/></td>
                      <td><xsl:value-of select="sellerinfo/email"/></td>
                      <td><xsl:value-of select="sellerinfo/phone"/></td>
                      <td><xsl:value-of select="sellerinfo/adress"/></td>
                 </xsl:if>
               </xsl:if>
            </xsl:if>
          </tr>
        </xsl:for-each>

        </table>
    </body>

</html>
