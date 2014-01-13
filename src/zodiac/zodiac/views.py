def root_view( request ):
	import datetime
	from datetime import date
	dia = request.POST.get("dia");
	if not dia:
		return {"project":"Zodiac","dia":"","mes":"","imatges":""}
	
	mes = request.POST.get("mes");
	naix = date(2010,int(mes),int(dia))

	""""Taules de Zodiac"""
	zod=[date(2010,1,21),date(2010,2,20),date(2010,3,21),date(2010,4,21),date(2010,5,22),date(2010,6,22),date(2010,7,23),date(2010,8,24),date(2010,9,24),date(2010,10,24),date(2010,11,23),date(2010,12,22)]

	zodname=["/static/aquarius.jpg","static/piscis.jpg","/static/aries.jpg","static/tauro.jpg","static/gemini.jpg","static/cancer.jpg","static/leo.jpg","static/virgo.jpgl","static/libra.jpg","static/escorpio.jpg","static/sagitari.jpg","static/capricorn.jpg"]

	i=0
	while zod[i] <= naix:
		i=i+1
	i=i-1
		
	return {"project":"Zodiac","dia":dia,"mes":mes,"imatges":zodname[i]}
