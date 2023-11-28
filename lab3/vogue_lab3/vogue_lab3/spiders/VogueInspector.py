# -*- coding: utf-8 -*-
import scrapy

class VogueInspectorSpider(scrapy.Spider):
    name = 'VogueInspector'
    allowed_domains = ['vogue.es']
    start_urls = ['https://www.vogue.es/galerias/tendencias-mas-arriesgadas-otono-invierno-2023-2024?utm_source=pocket-newtab-es-es']

    def parse(self, response):
        for vogue in response.css('div[class="GallerySlideFigCaption-dOeyTg dJsBXf"]'):
            # Crear un diccionario para almacenar los datos
            doc = {}  
            
            # Seleccionar el elemento h2 dentro de vogue
            data = vogue.css('h2.iUEiRd')

            # Extraer el título desde el span dentro del h2 y almacenarlo en 'title'
            doc['title'] = data.css('span.GallerySlideCaptionHedText-iqjOmM.jwPuvZ::text').extract_first()

            # Extraer el texto de todos los elementos p y almacenarlo en una lista en 'article'
            doc['article'] = vogue.css('p::text').extract()

            # Extraer las URL de los elementos a dentro de los elementos p y almacenarlas en una lista en 'url'
            doc['url'] = vogue.css('p a::attr(href)').extract()

            # Procesar cada URL individualmente
            for url in doc['url']:
                yield scrapy.Request(url, callback=self.parse_detail, meta={'title': doc['title'], 'article': doc['article']})

    def parse_detail(self, response):
        # Crear un diccionario para almacenar datos detallados
        detail = {}  

        # Obtener el título desde los metadatos y almacenarlo en 'TITLE'
        detail['TITLE'] = response.meta['title']

        # Obtener el artículo desde los metadatos y almacenarlo en 'ARTICLE'
        detail['ARTICLE'] = response.meta['article']

        # Obtener la URL de la página actual y almacenarla en 'URL'
        detail['URL'] = response.url

        # Extraer el título de la página y almacenarlo en 'URL_TITLE'
        detail['URL_TITLE'] = ' '.join(response.css('h1.BaseWrap-sc-gjQpdd.BaseText-ewhhUZ.SplitScreenContentHeaderHed-lcUSuI.iUEiRd.bwDymH.dfelga::text').extract())

        # Extraer el texto dentro de los elementos p y concatenarlo en 'DESCRIPTION'
        detail['DESCRIPTION'] = ' '.join(response.css('p *::text').extract())

        # Devolver el diccionario 'detail' como resultado del análisis de la página actual
        yield detail  





