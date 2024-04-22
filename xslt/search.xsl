<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:tei="http://www.tei-c.org/ns/1.0" xmlns:xs="http://www.w3.org/2001/XMLSchema" version="2.0" exclude-result-prefixes="xsl tei xs">
    <xsl:output encoding="UTF-8" media-type="text/html" method="html" version="5.0" indent="yes" omit-xml-declaration="yes"/>
    <xsl:import href="./partials/html_navbar.xsl"/>
    <xsl:import href="./partials/html_head.xsl"/>
    <xsl:import href="partials/html_footer.xsl"/>
    <xsl:template match="/">
        <xsl:variable name="doc_title" select="'Volltextsuche'"/>
        <html class="h-100">
            <head>
                <xsl:call-template name="html_head">
                    <xsl:with-param name="html_title" select="$doc_title"></xsl:with-param>
                </xsl:call-template>
            </head>

            <body class="d-flex flex-column h-100">
                <xsl:call-template name="nav_bar"/>
                <div id="searchPage">
                    <h1>
                        <xsl:value-of select="$doc_title"/>
                    </h1>
                    <div id="searchContainer" class="row">
                        <div class="col-3">
                            <div id="searchbox"></div>
                            <div id="decade">
                                <h4>Jahr</h4>
                            </div>
                            <div id="printer">
                                <h4>Drucker</h4>
                            </div>
                            <div id="printing_location">
                                <h4>Druckort</h4>
                            </div>
                            <div id="sort-by">Sortierung</div>
                            <div id="clear-refinements"></div>
                        </div>
                        <div class="col-8">
                            <div>
                                <div class="d-flex flex-column align-items-center" id="current-refinements"></div>
                            </div>
                            <div id="hits"></div>
                            <div id="pagination"></div>
                        </div>
                    </div>
                </div>


                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/instantsearch.css@7/themes/algolia-min.css"></link>
                <script src="https://cdn.jsdelivr.net/npm/instantsearch.js@4.46.0"></script>
                <script src="https://cdn.jsdelivr.net/npm/typesense-instantsearch-adapter@2/dist/typesense-instantsearch-adapter.min.js"></script>
                <script src="js/search.js"></script>
                <xsl:call-template name="html_footer"/>
            </body>

        </html>
    </xsl:template>
</xsl:stylesheet>