import flask
from newspaper import Article
import newspaper
from flask import request
import htmlmin

app = flask.Flask(__name__)
@app.route("/predict", methods=["POST"])
def parse_html():

	url = 'https://www.prothomalo.com/education/article/1565698/%E0%A6%AD%E0%A6%BE%E0%A6%B2%E0%A7%8B-%E0%A6%86%E0%A6%87%E0%A6%A1%E0%A6%BF%E0%A7%9F%E0%A6%BE-%E0%A6%AC%E0%A7%8D%E0%A6%AF%E0%A6%B0%E0%A7%8D%E0%A6%A5-%E0%A6%89%E0%A6%A6%E0%A7%8D%E0%A6%AF%E0%A7%8B%E0%A6%97'
	
	
	html_string = request.form.get('html')
	url = request.form.get('url')
	article = Article(url,language='bn')
	# html_string
	article.download(html_string)
	article.parse()
	article.nlp()
	item = dict()
	item['url'] = article.url
	item['title'] = article.title
	item['published_date'] = article.publish_date.strftime('%Y/%m/%d')
	item['text'] = article.text
	# item['html'] = htmlmin.minify(article.html, remove_empty_space=True)
	item['movies'] = list(article.movies)
	item['source_url'] = article.source_url
	if(len(article.tags) > 0):
		item['tags'] = list(article.tags)
	item['summary'] = article.summary
	item['top_image'] = article.top_image
	item['images'] = list(article.images)
	item['keywords'] = list(article.keywords)
	return flask.jsonify(item)

@app.route("/", methods=["GET","POST"])
def parse_html_default():

	url = 'https://www.prothomalo.com/education/article/1565698/%E0%A6%AD%E0%A6%BE%E0%A6%B2%E0%A7%8B-%E0%A6%86%E0%A6%87%E0%A6%A1%E0%A6%BF%E0%A7%9F%E0%A6%BE-%E0%A6%AC%E0%A7%8D%E0%A6%AF%E0%A6%B0%E0%A7%8D%E0%A6%A5-%E0%A6%89%E0%A6%A6%E0%A7%8D%E0%A6%AF%E0%A7%8B%E0%A6%97'
	article = Article(url,language='bn')
	html_string = request.args.get('html')
	
	html_string = """
<!DOCTYPE html>
<html lang=bn><head prefix="og: http://ogp.me/ns#">
<meta http-equiv=X-UA-Compatible content="IE=edge"/>
<meta charset=utf-8>
<meta name=viewport content="width=device-width, minimum-scale=1, initial-scale=1, maximum-scale=1, user-scalable=0"/>
<title>সুবর্ণচরে ধর্ষণের ঘটনার সঙ্গে ভোটের সম্পর্ক পায়নি মানবাধিকার কমিশন</title>
<meta name=keywords content=""/>
<meta name=description content="জাতীয় মানবাধিকার কমিশনের তথ্যানুসন্ধান প্রতিবেদন বলছে, সুবর্ণচরে ধর্ষণের শিকার নারীকে গুরুতর আঘাত করা এবং তাঁকে ধর্ষণ করার অভিযোগের প্রাথমিক সত্যতা পাওয়া গেছে। তবে একাদশ জাতীয় সংসদ নির্বাচনের সঙ্গে এই মারধর ও ধর্ষণের শিকার হওয়ার কোনো সম্পর্ক তদন্তকালে তদন্ত কমিটি খুঁজে পায়নি। বরং ওই নারীর স্বামীর দায়ের করা এজাহারের ভাষ্য মতে, পূর্ব শত্রুতার জেরেই এ ঘটনা ঘটেছে।"/>
<meta property=og:title content="সুবর্ণচরে ধর্ষণের ঘটনার সঙ্গে ভোটের সম্পর্ক পায়নি মানবাধিকার কমিশন"/>
<meta property=og:site_name content="প্রথম আলো"/>
<meta property=og:description content="জাতীয় মানবাধিকার কমিশনের তথ্যানুসন্ধান প্রতিবেদন বলছে, সুবর্ণচরে ধর্ষণের শিকার নারীকে গুরুতর আঘাত করা এবং তাঁকে ধর্ষণ করার অভিযোগের প্রাথমিক সত্যতা পাওয়া গেছে। তবে একাদশ জাতীয় সংসদ নির্বাচনের সঙ্গে এই মারধর ও ধর্ষণের শিকার হওয়ার কোনো সম্পর্ক তদন্তকালে তদন্ত কমিটি খুঁজে পায়নি। বরং ওই নারীর স্বামীর দায়ের করা এজাহারের ভাষ্য মতে, পূর্ব শত্রুতার জেরেই এ ঘটনা ঘটেছে।"/>
<meta property=og:type content=article />
<meta property=og:url content="https://www.prothomalo.com/bangladesh/article/1574390/%E0%A6%B8%E0%A7%81%E0%A6%AC%E0%A6%B0%E0%A7%8D%E0%A6%A3%E0%A6%9A%E0%A6%B0%E0%A7%87-%E0%A6%A7%E0%A6%B0%E0%A7%8D%E0%A6%B7%E0%A6%A3%E0%A7%87%E0%A6%B0-%E0%A6%98%E0%A6%9F%E0%A6%A8%E0%A6%BE%E0%A6%B0-%E0%A6%B8%E0%A6%99%E0%A7%8D%E0%A6%97%E0%A7%87-%E0%A6%AD%E0%A7%8B%E0%A6%9F%E0%A7%87%E0%A6%B0-%E0%A6%B8%E0%A6%AE%E0%A7%8D%E0%A6%AA%E0%A6%B0%E0%A7%8D%E0%A6%95-%E0%A6%AA%E0%A6%BE%E0%A7%9F%E0%A6%A8%E0%A6%BF"/>
<meta property=og:image content="https://paloimages.prothom-alo.com/contents/cache/images/600x315x1xxxxx1/uploads/media/2018/03/18/cc1107dbb1c246a9093a95ef8df7e78e-5aae1122a6fb1.jpg?jadewits_media_id=1199871"/>
<meta property=og:image:width content=600 />
<meta property=og:image:height content=315 />
<meta name=fb:app_id property=fb:app_id content=1499138263726489 />
<meta name=twitter:card content=summary_large_image />
<meta name=twitter:site content="@prothomalo"/>
<meta name=twitter:creator content="@prothomalo"/>
<meta name=twitter:url content="https://www.prothomalo.com/bangladesh/article/1574390/%E0%A6%B8%E0%A7%81%E0%A6%AC%E0%A6%B0%E0%A7%8D%E0%A6%A3%E0%A6%9A%E0%A6%B0%E0%A7%87-%E0%A6%A7%E0%A6%B0%E0%A7%8D%E0%A6%B7%E0%A6%A3%E0%A7%87%E0%A6%B0-%E0%A6%98%E0%A6%9F%E0%A6%A8%E0%A6%BE%E0%A6%B0-%E0%A6%B8%E0%A6%99%E0%A7%8D%E0%A6%97%E0%A7%87-%E0%A6%AD%E0%A7%8B%E0%A6%9F%E0%A7%87%E0%A6%B0-%E0%A6%B8%E0%A6%AE%E0%A7%8D%E0%A6%AA%E0%A6%B0%E0%A7%8D%E0%A6%95-%E0%A6%AA%E0%A6%BE%E0%A7%9F%E0%A6%A8%E0%A6%BF"/>
<meta name=twitter:title content="সুবর্ণচরে ধর্ষণের ঘটনার সঙ্গে ভোটের সম্পর্ক পায়নি মানবাধিকার কমিশন"/>
<meta name=twitter:description content="জাতীয় মানবাধিকার কমিশনের তথ্যানুসন্ধান প্রতিবেদন বলছে, সুবর্ণচরে ধর্ষণের শিকার নারীকে গুরুতর আঘাত করা এবং তাঁকে ধর্ষণ করার অভিযোগের প্রাথমিক সত্যতা পাওয়া গেছে। তবে একাদশ জাতীয় সংসদ নির্বাচনের সঙ্গে এই মারধর ও ধর্ষণের শিকার হওয়ার কোনো সম্পর্ক তদন্তকালে তদন্ত কমিটি খুঁজে পায়নি। বরং ওই নারীর স্বামীর দায়ের করা এজাহারের ভাষ্য মতে, পূর্ব শত্রুতার জেরেই এ ঘটনা ঘটেছে।"/>
<meta name=twitter:image content="https://paloimages.prothom-alo.com/contents/cache/images/600x315x1xxxxx1/uploads/media/2018/03/18/cc1107dbb1c246a9093a95ef8df7e78e-5aae1122a6fb1.jpg?jadewits_media_id=1199871"/>
<link rel=canonical href="https://www.prothomalo.com/bangladesh/article/1574390/%E0%A6%B8%E0%A7%81%E0%A6%AC%E0%A6%B0%E0%A7%8D%E0%A6%A3%E0%A6%9A%E0%A6%B0%E0%A7%87-%E0%A6%A7%E0%A6%B0%E0%A7%8D%E0%A6%B7%E0%A6%A3%E0%A7%87%E0%A6%B0-%E0%A6%98%E0%A6%9F%E0%A6%A8%E0%A6%BE%E0%A6%B0-%E0%A6%B8%E0%A6%99%E0%A7%8D%E0%A6%97%E0%A7%87-%E0%A6%AD%E0%A7%8B%E0%A6%9F%E0%A7%87%E0%A6%B0-%E0%A6%B8%E0%A6%AE%E0%A7%8D%E0%A6%AA%E0%A6%B0%E0%A7%8D%E0%A6%95-%E0%A6%AA%E0%A6%BE%E0%A7%9F%E0%A6%A8%E0%A6%BF">
<link rel=amphtml href="http://www.prothomalo.com/amp/bangladesh/article/1574390/%E0%A6%B8%E0%A7%81%E0%A6%AC%E0%A6%B0%E0%A7%8D%E0%A6%A3%E0%A6%9A%E0%A6%B0%E0%A7%87-%E0%A6%A7%E0%A6%B0%E0%A7%8D%E0%A6%B7%E0%A6%A3%E0%A7%87%E0%A6%B0-%E0%A6%98%E0%A6%9F%E0%A6%A8%E0%A6%BE%E0%A6%B0-%E0%A6%B8%E0%A6%99%E0%A7%8D%E0%A6%97%E0%A7%87-%E0%A6%AD%E0%A7%8B%E0%A6%9F%E0%A7%87%E0%A6%B0-%E0%A6%B8%E0%A6%AE%E0%A7%8D%E0%A6%AA%E0%A6%B0%E0%A7%8D%E0%A6%95-%E0%A6%AA%E0%A6%BE%E0%A7%9F%E0%A6%A8%E0%A6%BF">
<link rel="shortcut icon" href="/favicon.ico"/>
<link rel=icon type="image/ico" href="/favicon.ico"/>
<link rel=alternate type="application/rss+xml" title="প্রথম আলো RSS" href="https://www.prothomalo.com/feed/bangladesh"/>
<style>
						body{font-family:SolaimanLipi,Arial,Vrinda,FallbackBengaliFont,Helvetica,sans-serif;}
					</style>
<link href="//paloimages.prothom-alo.com/contents/assets/jquery/css/smoothness/jquery-ui-1.9.2.custom.min.css" media=all rel=stylesheet type="text/css"/><link href="//paloimages.prothom-alo.com/contents/assets/jquery/js/swiper/swiper.min.css" media=all rel=stylesheet type="text/css"/><link href="//paloimages.prothom-alo.com/contents/plugins/core/comments/css/comments_styles.css?v=1.7" media=all rel=stylesheet type="text/css"/><link href="//paloimages.prothom-alo.com/contents/widgets/styles/style.css?v=1.52" media=all rel=stylesheet type="text/css"/><link href="//paloimages.prothom-alo.com/contents/themes/public/style/font-jade-embedded.css?v=1.52" media=all rel=stylesheet type="text/css"/><link href="//paloimages.prothom-alo.com/contents/themes/public/style/style.css?v=1.52" media=all rel=stylesheet type="text/css"/><link href="//paloimages.prothom-alo.com/contents/themes/public/style/widget_style.css?v=1.52" media=all rel=stylesheet type="text/css"/><link href="//paloimages.prothom-alo.com/contents/themes/public/style/colors.css?v=1.52" media=all rel=stylesheet type="text/css"/><link href="//paloimages.prothom-alo.com/contents/themes/public/style/common_styles.css?v=1.52" media=all rel=stylesheet type="text/css"/><link href="//paloimages.prothom-alo.com/contents/themes/public/style/print.css?v=1.52" media=print rel=stylesheet type="text/css"/><script>
		var __jw_s_link = 'https://profiles.prothomalo.com/api/authentication_helper/session_js/?APP_ID=1&_nc=1547371242.33';
		var __jw_a_link = 'https://profiles.prothomalo.com/api/authentication_helper/account_bar/?contianer=account_bar&APP_ID=1';
		var __is_jadewits_user_logged_in = false;
		var __user_login_check = false;
		var __user_login_check2 = false;
		</script><script src="//paloimages.prothom-alo.com/contents/themes/public/js/core.js"></script><script src="//paloimages.prothom-alo.com/contents/assets/jquery/js/jquery-1.9.1.min.js"></script><script src="//paloimages.prothom-alo.com/contents/assets/jquery/js/jquery-ui-1.9.2.custom.min.js"></script><meta name=generator content="JadeWits Technologies Web Application 2.0.1"/><script>
	var jw_template_dir = '//paloimages.prothom-alo.com/contents/themes/public/';
	var jw_relative_url = '/';
	var jw_full_url =  'https://www.prothomalo.com/';
	var jw_cdn_url = '//paloimages.prothom-alo.com/';
	</script><script src="//paloimages.prothom-alo.com/contents/assets/jwshare/share.js?v=1.3"></script><script src="//paloimages.prothom-alo.com/contents/assets/jquery/js/swiper/swiper.jquery.min.js"></script><script src="//paloimages.prothom-alo.com/contents/assets/jquery/js/fullscreen/jquery.fullscreen.js"></script><script src="//paloimages.prothom-alo.com/contents/assets/jquery/js/fullscreen/fullscreen.js"></script><script src="//paloimages.prothom-alo.com/contents/assets/jquery/js/jquery-ui-timepicker-addon.js"></script><script src="//paloimages.prothom-alo.com/contents/assets/jadewits/jquery.jw.ari.js?v=1.52"></script><script src="//paloimages.prothom-alo.com/contents/themes/public/js/custom.js?v=1.52"></script><script src="//paloimages.prothom-alo.com/contents/assets/customjs/fade.js?v=1.52"></script>
<script>
			var facebook_application_id = "1499138263726489";
			var current_page_url = 'https://www.prothomalo.com/bangladesh';
			var jw_base_url = '/';
			var cannonical_url = 'https://www.prothomalo.com/bangladesh/article/1574390/%E0%A6%B8%E0%A7%81%E0%A6%AC%E0%A6%B0%E0%A7%8D%E0%A6%A3%E0%A6%9A%E0%A6%B0%E0%A7%87-%E0%A6%A7%E0%A6%B0%E0%A7%8D%E0%A6%B7%E0%A6%A3%E0%A7%87%E0%A6%B0-%E0%A6%98%E0%A6%9F%E0%A6%A8%E0%A6%BE%E0%A6%B0-%E0%A6%B8%E0%A6%99%E0%A7%8D%E0%A6%97%E0%A7%87-%E0%A6%AD%E0%A7%8B%E0%A6%9F%E0%A7%87%E0%A6%B0-%E0%A6%B8%E0%A6%AE%E0%A7%8D%E0%A6%AA%E0%A6%B0%E0%A7%8D%E0%A6%95-%E0%A6%AA%E0%A6%BE%E0%A7%9F%E0%A6%A8%E0%A6%BF';
			var current_archive_time = '2019-01-13';
			var last_archive_time = '2019-01-13';
			var jw_language = 'bn';
			var jw_device = 'phone';
			var jw_site_name = 'প্রথম আলো';
			var jw_meta_title = 'সুবর্ণচরে ধর্ষণের ঘটনার সঙ্গে ভোটের সম্পর্ক পায়নি মানবাধিকার কমিশন';
			var jw_meta_description = 'জাতীয় মানবাধিকার কমিশনের তথ্যানুসন্ধান প্রতিবেদন বলছে, সুবর্ণচরে ধর্ষণের শিকার নারীকে গুরুতর আঘাত করা এবং তাঁকে ধর্ষণ করার অভিযোগের প্রাথমিক সত্যতা পাওয়া গেছে। তবে একাদশ জাতীয় সংসদ নির্বাচনের সঙ্গে এই মারধর ও ধর্ষণের শিকার হওয়ার কোনো সম্পর্ক তদন্তকালে তদন্ত কমিটি খুঁজে পায়নি। বরং ওই নারীর স্বামীর দায়ের করা এজাহারের ভাষ্য মতে, পূর্ব শত্রুতার জেরেই এ ঘটনা ঘটেছে।';
			var jw_meta_url = 'https://www.prothomalo.com/bangladesh/article/1574390/%E0%A6%B8%E0%A7%81%E0%A6%AC%E0%A6%B0%E0%A7%8D%E0%A6%A3%E0%A6%9A%E0%A6%B0%E0%A7%87-%E0%A6%A7%E0%A6%B0%E0%A7%8D%E0%A6%B7%E0%A6%A3%E0%A7%87%E0%A6%B0-%E0%A6%98%E0%A6%9F%E0%A6%A8%E0%A6%BE%E0%A6%B0-%E0%A6%B8%E0%A6%99%E0%A7%8D%E0%A6%97%E0%A7%87-%E0%A6%AD%E0%A7%8B%E0%A6%9F%E0%A7%87%E0%A6%B0-%E0%A6%B8%E0%A6%AE%E0%A7%8D%E0%A6%AA%E0%A6%B0%E0%A7%8D%E0%A6%95-%E0%A6%AA%E0%A6%BE%E0%A7%9F%E0%A6%A8%E0%A6%BF';
			var jw_meta_image = 'https://paloimages.prothom-alo.com/contents/cache/images/600x315x1/uploads/media/2018/03/18/cc1107dbb1c246a9093a95ef8df7e78e-5aae1122a6fb1.jpg?jadewits_media_id=1199871';
			
		</script>
<script data-schema=Organization type="application/ld+json">
{
	"@context": "http://schema.org/",
	"name":"প্রথম আলো",
	"@type": "Organization",
	"url": "https://www.prothomalo.com", 
	"sameAs": [
		"https://www.facebook.com/DailyProthomAlo",
		"https://twitter.com/ProthomAlo",
		"https://www.youtube.com/c/ProthomAlo",
		"https://www.pinterest.com/ProthomAlo/",
		"https://plus.google.com/+ProthomAlo",
		"https://www.instagram.com/prothomalo/"
	],
	"logo": "https://paloimages.prothom-alo.com/contents/cache/images/195X46/uploads/media/2018/01/10/9a91271baadf642f49b51b471ffaaea8-5a55fbf367d21.png",
	"contactPoint": [{
		"@type": "ContactPoint",
		"telephone": "+88-02-8180078",
		"contactType": "customer service"
	},{
		"@type": "ContactPoint",
		"telephone": "+88-02-8180079",
		"contactType": "customer service"
	},{
		"@type": "ContactPoint",
		"telephone": "+88-02-8180080",
		"contactType": "customer service"
	},{
		"@type": "ContactPoint",
		"telephone": "+88-02-8180081",
		"contactType": "customer service"
	}],
    "potentialAction": {
		"@type": "SearchAction",
		"target": "https://www.prothomalo.com/search/?q={search_term_string}",
		"query-input": "required name=search_term_string"
	}
}
</script>
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-11355905-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-11355905-1');
  gtag('config', 'AW-921330377');
</script>
<script>
  gtag('event', 'conversion', {'send_to': 'AW-921330377/1aEkCPzTxIcBEMnFqbcD'});
</script>
<script async src='https://www.googletagservices.com/tag/js/gpt.js'></script>
<script>
  var gptadslots = [];
  var googletag = googletag || {cmd:[]};
  var url_dfp = $(location).attr('href');

  function isHomepage(){
	if( url_dfp == "https://www.prothomalo.com" || url_dfp == "https://www.prothomalo.com/" || url_dfp.search("/home") != -1 || url_dfp == "http://bd.prothomalo.com/" || url_dfp == "http://sg.prothomalo.com/"  || url_dfp == "http://sg1.prothomalo.com/" || url_dfp == "http://sg2.prothomalo.com/" || url_dfp == "http://us.prothomalo.com/" || url_dfp == "http://www.prothom-alo.com/" || url_dfp.search("/home") != -1 || url_dfp == "http://bd.prothom-alo.com/" || url_dfp == "http://sg.prothom-alo.com/"  || url_dfp == "http://sg1.prothom-alo.com/" || url_dfp == "http://sg2.prothom-alo.com/" || url_dfp == "http://us.prothom-alo.com/"){
		return true;
	}else{
		return false;
	}
  }
function detectmob() { 
	if( navigator.userAgent.match(/Android/i)
		|| navigator.userAgent.match(/webOS/i)
		|| navigator.userAgent.match(/iPhone/i)
		|| navigator.userAgent.match(/iPad/i)
		|| navigator.userAgent.match(/iPod/i)
		|| navigator.userAgent.match(/BlackBerry/i)
		|| navigator.userAgent.match(/Windows Phone/i))
	{
		return true;
	}
	else {
		return false;
	}
}
</script>
<script>
  googletag.cmd.push(function() {

// T1
    var map_leaderboard_T1 = googletag.sizeMapping()
							.addSize([1024, 0], [[970, 90], [728, 90]])
                            .addSize([768, 0], [[728, 90], [468, 60]])
                            .addSize([600, 0], [[468, 60], [320, 100], [320, 50]])
                            .addSize([0, 0], [[320, 100], [320, 50]])
                            .build();

// B1, B2, M1
    var map_leaderboard_B1_B2_M1 = googletag.sizeMapping()
                            .addSize([1024, 0], [[970, 90], [728, 90]])
                            .addSize([768, 0], [[728, 90], [468, 60]])
                            .addSize([600, 0], [[468, 60]])
                            .addSize([0, 0], [[336, 280], [300, 250]])
                            .build();
// R1, R2, R3
    var map_large_rectangle_R1_R2_R3 = googletag.sizeMapping()
                            .addSize([360, 0], [[336, 280], [300, 250]])
                            .addSize([0, 0], [[300, 250]])
                            .build();

// F1
	var map_half_page_F1 = googletag.sizeMapping()
                            .addSize([768, 0], [[300, 600], [300, 250]])
                            .addSize([360, 0], [[336, 280], [300, 250]])
                            .addSize([0, 0], [[300, 250]])
                            .build();

// Homepage Archive
if (url_dfp.search("/home/") != -1 || url_dfp.search("/archive") != -1) {
	//Adslot 1 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Home_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-44697-1')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
    //Adslot 2 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Home_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-44697-2')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 4 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Home_336x280_R2', [[336,280],[300,250]], 'div-gpt-ad-44697-4')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 6 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Home_728x90_B2', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-44697-6')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
}					
// Homepage	
else if ( url_dfp == "https://www.prothomalo.com" ||  url_dfp == "https://www.prothomalo.com/" || url_dfp.search("/home") != -1 || url_dfp == "http://www.prothomalo.com/?googfc" || url_dfp == "http://www.prothomalo.com/?dfpdeb" || url_dfp == "http://www.prothom-alo.com") {

    //Adslot 1 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Home_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-44697-1')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	
	//Adslot 2 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Home_336x280_R1',[[336,280],[300,250]],'div-gpt-ad-44697-2')
							 .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
							 
	//Adslot 3 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Home_468x60_B1',[[970,90],[728,90],[468,60],[320,100],[320,50]],'div-gpt-ad-44697-3')
							 .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
							 
    //Adslot 4 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Home_336x280_R2', [[336,280],[300,250]], 'div-gpt-ad-44697-4')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));

	//Adslot 5 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Home_336x280_R3', [[336,280],[300,250]], 'div-gpt-ad-44697-5')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 6 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Home_728x90_B2', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-44697-6')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
							 
					 

}
else if (url_dfp.search("iftar-sahri-prayer-times") != -1 ) {
	
}
else if (url_dfp.search("hajj") != -1 ) {
	
}
// Sports Article / Gallery
else if (url_dfp.search("sports/article/") != -1 || url_dfp.search("sports/gallery/") != -1) {
	//Adslot 3 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Sports_Articles_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-19259-3')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 9 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Sports_Articles_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-19259-9')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 16 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Sports_Articles_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-19259-16')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 17 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Sports_Articles_336x280_R2', [[336,280],[300,250]], 'div-gpt-ad-19259-17')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
	//Adslot 19 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Sports_Articles_300x600_F1', [[300,600],[336,280],[300,250]], 'div-gpt-ad-19259-19')
                             .defineSizeMapping(map_half_page_F1)
                             .addService(googletag.pubads()));
}
// Sports Archive / Listing
else if (url_dfp.search("sports/article") != -1 || url_dfp.search("sports/gallery") != -1) {
	//Adslot 3 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Sports_Articles_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-19259-3')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 9 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Sports_Articles_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-19259-9')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 16 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Sports_Articles_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-19259-16')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
	//Adslot 19 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Sports_Articles_300x600_F1', [[300,600],[336,280],[300,250]], 'div-gpt-ad-19259-19')
                             .defineSizeMapping(map_half_page_F1)
                             .addService(googletag.pubads()));
}
// Fixture page Landing
else if(url_dfp.search("/sports-fixture") != -1){

}
// Live Score Sports
/*else if (url_dfp.search("/sports-results") != -1) {
	//Adslot 4 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Sports_Live_Scores_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-19259-4')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 11 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Sports_Live_Scores_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-19259-11')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 20 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Sports_Live_Scores_F1', [[300,600],[336,280],[300,250]], 'div-gpt-ad-19259-20')
                            .defineSizeMapping(map_half_page_F1)
                             .addService(googletag.pubads()));
	//Adslot 18 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Sports_Live_Scores_R1', [[336,280],[300,250]], 'div-gpt-ad-19259-18')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads())); 
} */
// Sports Sub Section
else if (url_dfp.search("/sports-") != -1) {
	//Adslot 2 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Sports_Sub_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-19259-2')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 7 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Sports_Sub_468x60_B1', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-19259-7')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
    //Adslot 8 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Sports_Sub_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-19259-8')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 10 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Sports_Sub_728x90_M1', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-19259-10')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 15 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Sports_Sub_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-19259-15')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
}
// Sports Landing
else if (url_dfp.search("/sports") != -1 || url_dfp.search("/bangladesh-cricket-series") != -1) {
	//Adslot 1 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Sports_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-19259-1')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 5 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Sports_468x60_B1', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-19259-5')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
    //Adslot 6 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Sports_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-19259-6')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 12 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Sports_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-19259-12')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 13 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Sports_336x280_R2', [[336,280],[300,250]], 'div-gpt-ad-19259-13')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 14 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Sports_336x280_R3', [[336,280],[300,250]], 'div-gpt-ad-19259-14')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
}
// Sports Landing
else if (url_dfp.search("/fifa-world-cup") != -1) {
	//Adslot 1 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Sports_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-19259-1')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 5 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Sports_468x60_B1', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-19259-5')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
    //Adslot 6 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Sports_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-19259-6')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 12 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Sports_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-19259-12')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 13 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Sports_336x280_R2', [[336,280],[300,250]], 'div-gpt-ad-19259-13')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 14 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Sports_336x280_R3', [[336,280],[300,250]], 'div-gpt-ad-19259-14')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
}



// Sports Landing
else if (url_dfp.search("/asia-cup") != -1) {
	//Adslot 1 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Sports_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-19259-1')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 5 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Sports_468x60_B1', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-19259-5')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
    //Adslot 6 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Sports_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-19259-6')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 12 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Sports_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-19259-12')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 13 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Sports_336x280_R2', [[336,280],[300,250]], 'div-gpt-ad-19259-13')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 14 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Sports_336x280_R3', [[336,280],[300,250]], 'div-gpt-ad-19259-14')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
}




// Technology Article / Gallery
else if (url_dfp.search("technology/article/") != -1 || url_dfp.search("technology/gallery/") != -1) {
	//Adslot 3 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Tech_Articles_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-34418-3')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 9 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Tech_Articles_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-34418-9')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 14 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Tech_Articles_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-34418-14')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 15 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Tech_Articles_336x280_R2', [[336,280],[300,250]], 'div-gpt-ad-34418-15')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 16 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Tech_Articles_300x600_F1', [[300,600],[336,280],[300,250]], 'div-gpt-ad-34418-16')
                             .defineSizeMapping(map_half_page_F1)
                             .addService(googletag.pubads()));
}
// Technology Archive / Listing
else if (url_dfp.search("technology/article") != -1 || url_dfp.search("technology/gallery") != -1) {
	//Adslot 3 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Tech_Articles_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-34418-3')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 9 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Tech_Articles_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-34418-9')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 14 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Tech_Articles_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-34418-14')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 16 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Tech_Articles_300x600_F1', [[300,600],[336,280],[300,250]], 'div-gpt-ad-34418-16')
                             .defineSizeMapping(map_half_page_F1)
                             .addService(googletag.pubads()));
}
// Technology Sub-category
else if (url_dfp.search("/technology-") != -1) {
	//Adslot 2 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Tech_Sub_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-34418-2')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 6 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Tech_Sub_468x60_B1', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-34418-6')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
    //Adslot 7 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Tech_Sub_728x90_M1', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-34418-7')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
    //Adslot 8 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Tech_Sub_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-34418-8')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 13 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Tech_Sub_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-34418-13')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
}
// Technology Landing
else if (url_dfp.search("/technology") != -1) {
	//Adslot 1 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Technology_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-34418-1')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 4 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Technology_468x60_B1', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-34418-4')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
    //Adslot 5 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Technology_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-34418-5')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 10 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Technology_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-34418-10')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 11 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Technology_336x280_R2', [[336,280],[300,250]], 'div-gpt-ad-34418-11')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 12 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Technology_336x280_R3', [[336,280],[300,250]], 'div-gpt-ad-34418-12')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
}
// Life Style Article / Gallery
else if (url_dfp.search("life-style/article/") != -1 || url_dfp.search("life-style/gallery/") != -1
|| url_dfp.search("we-are/article/") != -1 || url_dfp.search("we-are/gallery/") != -1
|| url_dfp.search("art-and-literature/article/") != -1 || url_dfp.search("art-and-literature/gallery/") != -1) {
	//Adslot 3 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Lifestyle_Articles_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-23351-3')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 9 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Lifestyle_Articles_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-23351-9')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 14 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Lifestyle_Articles_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-23351-14')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 15 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Lifestyle_Articles_336x280_R2', [[336,280],[300,250]], 'div-gpt-ad-23351-15')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 16 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Lifestyle_Articles_300x600_F1', [[300,600],[336,280],[300,250]], 'div-gpt-ad-23351-16')
                             .defineSizeMapping(map_half_page_F1)
                             .addService(googletag.pubads()));
}
// Life Style Archive / Listing
else if (url_dfp.search("life-style/article") != -1 || url_dfp.search("life-style/gallery") != -1
|| url_dfp.search("we-are/article") != -1 || url_dfp.search("we-are/gallery") != -1
|| url_dfp.search("art-and-literature/article") != -1 || url_dfp.search("art-and-literature/gallery") != -1) {
	//Adslot 3 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Lifestyle_Articles_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-23351-3')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 9 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Lifestyle_Articles_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-23351-9')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 14 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Lifestyle_Articles_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-23351-14')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 16 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Lifestyle_Articles_300x600_F1', [[300,600],[336,280],[300,250]], 'div-gpt-ad-23351-16')
                             .defineSizeMapping(map_half_page_F1)
                             .addService(googletag.pubads()));
}
//kishoralo

else if (url_dfp.search("kishoralo/article/") != -1 || url_dfp.search("kishoralo/gallery/") != -1) {
	
    gptadslots.push(googletag.defineSlot('/85406138/Kishoralo_Articles_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-5720320-13')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
							 
    gptadslots.push(googletag.defineSlot('/85406138/Kishoralo_Articles_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-5720320-16')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
							 
    gptadslots.push(googletag.defineSlot('/85406138/Kishoralo_Articles_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-5720320-20')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
							 
    gptadslots.push(googletag.defineSlot('/85406138/Kishoralo_Articles_336x280_R2', [[336,280],[300,250]], 'div-gpt-ad-5720320-21')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
							 
    gptadslots.push(googletag.defineSlot('/85406138/Kishoralo_Articles_300x600_F1', [[300,600],[336,280],[300,250]], 'div-gpt-ad-5720320-22')
                             .defineSizeMapping(map_half_page_F1)
                             .addService(googletag.pubads()));					 						 
							 
}

else if (url_dfp.search("kishoralo/article") != -1 || url_dfp.search("kishoralo/gallery") != -1) {
	
	
    gptadslots.push(googletag.defineSlot('/85406138/Kishoralo_Articles_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-5720320-13')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
 
    gptadslots.push(googletag.defineSlot('/85406138/Kishoralo_Articles_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-5720320-16')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
							 
    gptadslots.push(googletag.defineSlot('/85406138/Kishoralo_Articles_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-5720320-20')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
							 	
    gptadslots.push(googletag.defineSlot('/85406138/Kishoralo_Articles_300x600_F1', [[300,600],[336,280],[300,250]], 'div-gpt-ad-5720320-22')
                             .defineSizeMapping(map_half_page_F1)
                             .addService(googletag.pubads()));		
}

else if (url_dfp.search("/kia-") != -1) {

    gptadslots.push(googletag.defineSlot('/85406138/Kishoralo_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-5720320-12')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));

    gptadslots.push(googletag.defineSlot('/85406138/Kishoralo_468x60_B1', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-5720320-14')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
							 
    gptadslots.push(googletag.defineSlot('/85406138/Kishoralo_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-5720320-15')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));

    gptadslots.push(googletag.defineSlot('/85406138/Kishoralo_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-5720320-17')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));	
	
}

else if (url_dfp.search("/kishoralo") != -1) {	

    gptadslots.push(googletag.defineSlot('/85406138/Kishoralo_468x60_B1', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-5720320-14')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
							 
    gptadslots.push(googletag.defineSlot('/85406138/Kishoralo_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-5720320-15')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));

    gptadslots.push(googletag.defineSlot('/85406138/Kishoralo_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-5720320-17')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));	
							 
	    gptadslots.push(googletag.defineSlot('/85406138/Kishoralo_336x280_R2', [[336,280],[300,250]], 'div-gpt-ad-5720320-18')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));

    gptadslots.push(googletag.defineSlot('/85406138/Kishoralo_336x280_R3', [[336,280],[300,250]], 'div-gpt-ad-5720320-19')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));

}


// Life Style Sub-category
else if (url_dfp.search("/lifestyle-") != -1 || url_dfp.search("/we-are-") != -1 || url_dfp.search("/female-stage") != -1 || url_dfp.search("/personality") != -1 || url_dfp.search("/torun") != -1 || url_dfp.search("/international-womens-day") != -1 || url_dfp.search("/art-and-literature-") != -1 || url_dfp.search("/poem") != -1 || url_dfp.search("/short-stories") != -1 || url_dfp.search("/industrial-art") != -1 || url_dfp.search("/meeting") != -1 || url_dfp.search("/treatise") != -1 || url_dfp.search("/translation") != -1 || url_dfp.search("/children-s-literature") != -1 || url_dfp.search("/book-discussion") != -1 || url_dfp.search("/kishor") != -1 || url_dfp.search("/child") != -1  || url_dfp.search("/personality") != -1 || url_dfp.search("/torun") != -1 || url_dfp.search("/probashi") != -1) {
	//Adslot 2 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Lifestyle_Sub_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-23351-2')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 6 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Lifestyle_Sub_468x60_B1', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-23351-6')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
    //Adslot 7 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Lifestyle_Sub_728x90_M1', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-23351-7')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
    //Adslot 8 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Lifestyle_Sub_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-23351-8')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 13 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Lifestyle_Sub_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-23351-13')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
}
// Life Style Landing
else if (url_dfp.search("/life-style") != -1 || url_dfp.search("/we-are") != -1 || url_dfp.search("/art-and-literature") != -1) {
	//Adslot 1 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Lifestyle_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-23351-1')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 4 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Lifestyle_468x60_B1', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-23351-4')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
    //Adslot 5 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Lifestyle_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-23351-5')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 10 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Lifestyle_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-23351-10')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 11 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Lifestyle_336x280_R2', [[336,280],[300,250]], 'div-gpt-ad-23351-11')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 12 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Lifestyle_336x280_R3', [[336,280],[300,250]], 'div-gpt-ad-23351-12')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
}
// Entertainment Article / Gallery
else if (url_dfp.search("entertainment/article/") != -1 || url_dfp.search("entertainment/gallery/") != -1) {
	//Adslot 3 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Ent_Articles_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-31848-3')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 8 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Ent_Articles_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-31848-8')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 14 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Ent_Articles_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-31848-14')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 15 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Ent_Articles_336x280_R2', [[336,280],[300,250]], 'div-gpt-ad-31848-15')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 16 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Ent_Articles_300x600_F1', [[300,600],[336,280],[300,250]], 'div-gpt-ad-31848-16')
                             .defineSizeMapping(map_half_page_F1)
                             .addService(googletag.pubads()));
}
// Entertainment Archive / Listing
else if (url_dfp.search("entertainment/article") != -1 || url_dfp.search("entertainment/gallery") != -1) {
	//Adslot 3 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Ent_Articles_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-31848-3')

                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 8 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Ent_Articles_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-31848-8')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 14 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Ent_Articles_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-31848-14')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 16 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Ent_Articles_300x600_F1', [[300,600],[336,280],[300,250]], 'div-gpt-ad-31848-16')
                             .defineSizeMapping(map_half_page_F1)
                             .addService(googletag.pubads()));
}
// Entertainment Sub Category
else if(url_dfp.search("/entertainment-") != -1 || url_dfp.search("/alapon") != -1 || url_dfp.search("/music") != -1 || url_dfp.search("/dance") != -1 || url_dfp.search("/somalochona") != -1 || url_dfp.search("/tarokader-lekha") != -1){
	//Adslot 2 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Ent_Sub_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-31848-2')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 6 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Ent_Sub_468x60_B1', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-31848-6')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
    //Adslot 7 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Ent_Sub_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-31848-7')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 9 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Ent_Sub_728x90_M1', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-31848-9')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 13 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Ent_Sub_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-31848-13')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
}
// Entertainment Landing
else if (url_dfp.search("/entertainment") != -1) {

	//Adslot 1 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Entertainment_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-31848-1')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 4 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Entertainment_468x60_B1', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-31848-4')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
    //Adslot 5 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Entertainment_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-31848-5')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 10 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Entertainment_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-31848-10')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 11 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Entertainment_336x280_R2', [[336,280],[300,250]], 'div-gpt-ad-31848-11')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 12 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Entertainment_336x280_R3', [[336,280],[300,250]], 'div-gpt-ad-31848-12')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
	
}
// Business Article / Gallery
else if (url_dfp.search("economy/article/") != -1 || url_dfp.search("economy/gallery/") != -1) {
	//Adslot 3 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Business_Articles_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-85668-3')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 9 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Business_Articles_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-85668-9')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	 //Adslot 14 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Business_Articles_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-85668-14')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 15 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Business_Articles_336x280_R2', [[336,280],[300,250]], 'div-gpt-ad-85668-15')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 16 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Business_Articles_300x600_F1', [[300,600],[336,280],[300,250]], 'div-gpt-ad-85668-16')
                             .defineSizeMapping(map_half_page_F1)
                             .addService(googletag.pubads()));
}

// Business Archive / Listing
else if (url_dfp.search("economy/article") != -1 || url_dfp.search("economy/gallery") != -1) {
	//Adslot 3 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Business_Articles_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-85668-3')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 9 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Business_Articles_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-85668-9')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	 //Adslot 14 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Business_Articles_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-85668-14')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 16 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Business_Articles_300x600_F1', [[300,600],[336,280],[300,250]], 'div-gpt-ad-85668-16')
                             .defineSizeMapping(map_half_page_F1)
                             .addService(googletag.pubads()));
}
// Business Sub-category
else if (url_dfp.search("/economy-") != -1 || url_dfp.search("/budget") != -1) {
	//Adslot 2 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Business_Sub_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-85668-2')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 6 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Business_Sub_468x60_B1', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-85668-6')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
    //Adslot 7 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Business_Sub_728x90_M1', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-85668-7')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
    //Adslot 8 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Business_Sub_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-85668-8')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 13 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Business_Sub_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-85668-13')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
}
// Business Landing
else if (url_dfp.search("/economy") != -1) {
	//Adslot 1 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Business_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-85668-1')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 4 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Business_468x60_B1', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-85668-4')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
    //Adslot 5 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Business_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-85668-5')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 10 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Business_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-85668-10')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 11 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Business_336x280_R2', [[336,280],[300,250]], 'div-gpt-ad-85668-11')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 12 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Business_336x280_R3', [[336,280],[300,250]], 'div-gpt-ad-85668-12')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
}

// Northamerica Article / Gallery
else if (url_dfp.search("northamerica/article/") != -1 || url_dfp.search("northamerica/gallery/") != -1) {
	//Adslot 3 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Northamerica_Articles_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-4549433-3')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
			    //Adslot 10 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Northamerica_Articles_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-4549433-10')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	    //Adslot 20 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Northamerica_Articles_300x600_F1', [[300,600],[336,280],[300,250]], 'div-gpt-ad-4549433-20')
                             .defineSizeMapping(map_half_page_F1)
                             .addService(googletag.pubads()));
	    //Adslot 17 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Northamerica_Articles_336x280_R2', [[336,280],[300,250]], 'div-gpt-ad-4549433-17')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
	    //Adslot 16 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Northamerica_Articles_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-4549433-16')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
}

// Northamerica Archive / Listing
else if (url_dfp.search("northamerica/article") != -1 || url_dfp.search("northamerica/gallery") != -1) {
	//Adslot 3 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Northamerica_Articles_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-4549433-3')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
			    //Adslot 10 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Northamerica_Articles_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-4549433-10')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	    //Adslot 20 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Northamerica_Articles_300x600_F1', [[300,600],[336,280],[300,250]], 'div-gpt-ad-4549433-20')
                             .defineSizeMapping(map_half_page_F1)
                             .addService(googletag.pubads()));

	    //Adslot 16 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Northamerica_Articles_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-4549433-16')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
}
// northamerica Sub-category
else if (url_dfp.search("/northamerica-") != -1 || url_dfp.search("/canada") != -1 || url_dfp.search("/america") != -1) {
	
	 //Adslot 2 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Northamerica_Sub_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-4549433-2')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 8 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Northamerica_Sub_728x90_M1', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-4549433-8')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
    //Adslot 9 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Northamerica_Sub_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-4549433-9')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	 //Adslot 7 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Northamerica_Sub_468x60_B1', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-4549433-7')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
							 
	    //Adslot 15 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Northamerica_Sub_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-4549433-15')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
}
// northamerica Landing
else if (url_dfp.search("/northamerica") != -1) {
	
	 gptadslots.push(googletag.defineSlot('/85406138/Northamerica_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-4549433-1')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
   
							 
	//Adslot 5 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Northamerica_468x60_B1', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-4549433-5')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
    //Adslot 6 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Northamerica_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-4549433-6')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
   
							 
	//Adslot 12 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Northamerica_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-4549433-12')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 13 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Northamerica_336x280_R2', [[336,280],[300,250]], 'div-gpt-ad-4549433-13')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 14 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Northamerica_336x280_R3', [[336,280],[300,250]], 'div-gpt-ad-4549433-14')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
	
}
// bondhushava Article / Gallery
else if (url_dfp.search("bondhushava/article/") != -1 || url_dfp.search("bondhushava/gallery/") != -1) {
	
	gptadslots.push(googletag.defineSlot('/85406138/Bondhushava_Articles_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-5720320-2')
							 .defineSizeMapping(map_leaderboard_T1)
							 .addService(googletag.pubads()));
 
 gptadslots.push(googletag.defineSlot('/85406138/Bondhushava_Articles_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-5720320-5')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
							 
 gptadslots.push(googletag.defineSlot('/85406138/Bondhushava_Articles_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-5720320-9')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));	
							 
	gptadslots.push(googletag.defineSlot('/85406138/Bondhushava_Articles_336x280_R2', [[336,280],[300,250]], 'div-gpt-ad-5720320-10')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));	
							 
	 gptadslots.push(googletag.defineSlot('/85406138/Bondhushava_Articles_300x600_F1', [[300,600],[336,280],[300,250]], 'div-gpt-ad-5720320-11')
                             .defineSizeMapping(map_half_page_F1)
                             .addService(googletag.pubads()));					 						 
							 
}
// bondhushava Archive / Listing
else if (url_dfp.search("bondhushava/article") != -1 || url_dfp.search("bondhushava/gallery") != -1) {
	gptadslots.push(googletag.defineSlot('/85406138/Bondhushava_Articles_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-5720320-2')
 .defineSizeMapping(map_leaderboard_T1)
 .addService(googletag.pubads()));
 
 gptadslots.push(googletag.defineSlot('/85406138/Bondhushava_Articles_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-5720320-5')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
							 
							 
gptadslots.push(googletag.defineSlot('/85406138/Bondhushava_Articles_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-5720320-9')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
							 	
 gptadslots.push(googletag.defineSlot('/85406138/Bondhushava_Articles_300x600_F1', [[300,600],[336,280],[300,250]], 'div-gpt-ad-5720320-11')
                             .defineSizeMapping(map_half_page_F1)
                             .addService(googletag.pubads()));		
}
// bondhushava Sub-category
else if (url_dfp.search("/bs-") != -1) {
	 gptadslots.push(googletag.defineSlot('/85406138/Bondhushava_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-5720320-1')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 6 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Bondhushava_468x60_B1', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-5720320-3')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
							 
							 
    gptadslots.push(googletag.defineSlot('/85406138/Bondhushava_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-5720320-4')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
							 
    gptadslots.push(googletag.defineSlot('/85406138/Bondhushava_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-5720320-6')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
}
// bondhushava Landing
else if (url_dfp.search("/bondhushava") != -1) {
	 gptadslots.push(googletag.defineSlot('/85406138/Bondhushava_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-5720320-1')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
    
    //Adslot 3 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Bondhushava_468x60_B1', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-5720320-3')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
    //Adslot 4 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Bondhushava_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-5720320-4')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
    
    //Adslot 6 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Bondhushava_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-5720320-6')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 7 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Bondhushava_336x280_R2', [[336,280],[300,250]], 'div-gpt-ad-5720320-7')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 8 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Bondhushava_336x280_R3', [[336,280],[300,250]], 'div-gpt-ad-5720320-8')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));

}

// Education Article / Gallery
else if (url_dfp.search("education/article/") != -1 || url_dfp.search("education/gallery/") != -1) {
	//Adslot 3 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Edu_Articles_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-81614-3')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 9 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Edu_Articles_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-81614-9')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 14 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Edu_Articles_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-81614-14')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 15 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Edu_Articles_336x280_R2', [[336,280],[300,250]], 'div-gpt-ad-81614-15')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 16 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Edu_Articles_300x600_F1', [[300,600],[336,280],[300,250]], 'div-gpt-ad-81614-16')
                             .defineSizeMapping(map_half_page_F1)
                             .addService(googletag.pubads()));
}
// Education Archive / Listing
else if (url_dfp.search("education/article") != -1 || url_dfp.search("education/gallery") != -1) {
	//Adslot 3 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Edu_Articles_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-81614-3')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 9 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Edu_Articles_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-81614-9')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 14 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Edu_Articles_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-81614-14')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 16 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Edu_Articles_300x600_F1', [[300,600],[336,280],[300,250]], 'div-gpt-ad-81614-16')
                             .defineSizeMapping(map_half_page_F1)
                             .addService(googletag.pubads()));
}
// Education Sub-category
else if (url_dfp.search("/education-") != -1 || url_dfp.search("/institution") != -1 || url_dfp.search("/meritorious") != -1 || url_dfp.search("/preparation") != -1 || url_dfp.search("/jenerakhun") != -1 || (url_dfp.search("-education") != -1 && url_dfp.search("opinion-education") == -1)) {
	//Adslot 2 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Edu_Sub_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-81614-2')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 6 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Edu_Sub_468x60_B1', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-81614-6')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
    //Adslot 7 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Edu_Sub_728x90_M1', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-81614-7')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
    //Adslot 8 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Edu_Sub_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-81614-8')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 13 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Edu_Sub_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-81614-13')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
}
// Education Landing
else if (url_dfp.search("/education") != -1) {
	//Adslot 1 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Education_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-81614-1')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 4 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Education_468x60_B1', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-81614-4')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
    //Adslot 5 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Education_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-81614-5')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 10 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Education_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-81614-10')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 11 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Education_336x280_R2', [[336,280],[300,250]], 'div-gpt-ad-81614-11')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 12 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Education_336x280_R3', [[336,280],[300,250]], 'div-gpt-ad-81614-12')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
}
// Protichinta Site
else if (url_dfp.search("/protichinta") != -1) {
	//Adslot 7 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Protichinta_Home_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-4549433-4')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));

	//Adslot 14 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Protichinta_Home_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-4549433-11')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 21 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Protichinta_Home_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-4549433-18')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
	//Adslot 28 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Protichinta_Home_336x280_R2', [[336,280],[300,250]], 'div-gpt-ad-4549433-19')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));

}
// Naksha Landing
else if (url_dfp.search("/naksha") != -1) {
	//Adslot 2 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Naksha_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-16530-2')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 9 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Naksha_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-16530-9')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 16 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Naksha_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-16530-16')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
	//Adslot 23 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Naksha_300x600_F1', [[300,600],[336,280],[300,250]], 'div-gpt-ad-16530-23')
                             .defineSizeMapping(map_half_page_F1)
                             .addService(googletag.pubads()));
}
// shapno Landing
else if (url_dfp.search("/shapno") != -1) {
	//Adslot 3 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Shapno_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-16530-3')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 10 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Shapno_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-16530-10')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 17 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Shapno_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-16530-17')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
	//Adslot 24 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Shapno_300x600_F1', [[300,600],[336,280],[300,250]], 'div-gpt-ad-16530-24')
                             .defineSizeMapping(map_half_page_F1)
                             .addService(googletag.pubads()));
}
// adhuna Landing
else if (url_dfp.search("/adhuna") != -1) {
	//Adslot 4 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Adhuna_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-16530-4')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 11 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Adhuna_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-16530-11')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 18 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Adhuna_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-16530-18')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
	//Adslot 25 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Adhuna_300x600_F1', [[300,600],[336,280],[300,250]], 'div-gpt-ad-16530-25')
                             .defineSizeMapping(map_half_page_F1)
                             .addService(googletag.pubads()));
}
// holiday Landing
else if (url_dfp.search("/holiday") != -1) {
	//Adslot 5 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Holiday_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-16530-5')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 12 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Holiday_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-16530-12')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 19 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Holiday_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-16530-19')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
	//Adslot 26 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Holiday_300x600_F1', [[300,600],[336,280],[300,250]], 'div-gpt-ad-16530-26')
                             .defineSizeMapping(map_half_page_F1)
                             .addService(googletag.pubads()));
}
// roshalo details article
else if (url_dfp.search("roshalo/article/") != -1 || url_dfp.search("roshalo/gallery/") != -1){
	//Adslot 1 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Roshalo_Articles_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-1837451-1')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
    //Adslot 2 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Roshalo_Articles_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-1837451-2')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
    //Adslot 3 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Roshalo_Articles_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-1837451-3')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 4 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Roshalo_Articles_336x280_R2', [[336,280],[300,250]], 'div-gpt-ad-1837451-4')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 5 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Roshalo_Articles_300x600_F1', [[300,600],[336,280],[300,250]], 'div-gpt-ad-1837451-5')
                             .defineSizeMapping(map_half_page_F1)
                             .addService(googletag.pubads()));
}// roshalo archive listing
else if (url_dfp.search("roshalo/article") != -1 || url_dfp.search("roshalo/gallery") != -1){
	//Adslot 1 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Roshalo_Articles_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-1837451-1')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
    //Adslot 2 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Roshalo_Articles_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-1837451-2')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
    //Adslot 3 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Roshalo_Articles_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-1837451-3')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 5 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Roshalo_Articles_300x600_F1', [[300,600],[336,280],[300,250]], 'div-gpt-ad-1837451-5')
                             .defineSizeMapping(map_half_page_F1)
                             .addService(googletag.pubads()));
}
// roshalo Landing
else if (url_dfp.search("/roshalo") != -1 && url_dfp.search("/roshalo/") == -1) {


	//Adslot 6 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Roshalo_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-16530-6')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 13 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Roshalo_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-16530-13')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 20 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Roshalo_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-16530-20')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
	//Adslot 27 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Roshalo_300x600_F1', [[300,600],[336,280],[300,250]], 'div-gpt-ad-16530-27')
                             .defineSizeMapping(map_half_page_F1)
                             .addService(googletag.pubads()));
}
// ananda Landing
else if (url_dfp.search("/ananda") != -1) {
	//Adslot 7 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Ananda_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-16530-7')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));

	//Adslot 14 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Ananda_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-16530-14')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 21 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Ananda_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-16530-21')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
	//Adslot 28 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Ananda_300x600_F1', [[300,600],[336,280],[300,250]], 'div-gpt-ad-16530-28')
                             .defineSizeMapping(map_half_page_F1)
                             .addService(googletag.pubads()));
}
// All Features Landing
else if (url_dfp.search("/features") != -1 || url_dfp.search("/sabar-age-shisu") != -1 || url_dfp.search("/gollachut") != -1 ||
url_dfp.search("/anna-alo") != -1 || url_dfp.search("/shilpo-o-sahitto") != -1 || url_dfp.search("/alokito-chittagong") != -1 ||
url_dfp.search("/amader-kotha-shono") != -1 || url_dfp.search("/bondhushava") != -1 || url_dfp.search("/projonmo-dot-com") != -1 || url_dfp.search("/choltibishow") != -1) {
	//Adslot 1 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Features_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-16530-1')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 8 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Features_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-16530-8')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 15 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Features_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-16530-15')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
	//Adslot 22 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Features_300x600_F1', [[300,600],[336,280],[300,250]], 'div-gpt-ad-16530-22')
                             .defineSizeMapping(map_half_page_F1)
                             .addService(googletag.pubads()));
}
// Photo View
else if (url_dfp.search("photo/gallery/") != -1 || url_dfp.search("cartoon/gallery/") != -1) {
	//Adslot 2 declaration
    gptadslots.push(googletag.defineSlot('/85406138/photos_views_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-79289-2')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 8 declaration
    gptadslots.push(googletag.defineSlot('/85406138/photos_views_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-79289-8')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 14 declaration
    gptadslots.push(googletag.defineSlot('/85406138/photos_views_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-79289-14')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 15 declaration
    gptadslots.push(googletag.defineSlot('/85406138/photos_views_336x280_R2', [[336,280],[300,250]], 'div-gpt-ad-79289-15')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
	//Adslot 19 declaration
    gptadslots.push(googletag.defineSlot('/85406138/photos_views_300x600_F1', [[300,600],[336,280],[300,250]], 'div-gpt-ad-79289-19')
                             .defineSizeMapping(map_half_page_F1)
                             .addService(googletag.pubads()));
}
// Photo Landing
else if (url_dfp.search("/photo") != -1  || url_dfp.search("/cartoon") != -1 ) {
	//Adslot 1 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Photos_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-79289-1')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 5 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Photos_468x60_B1', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-79289-5')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 6 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Photos_728x90_M1', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-79289-6')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
    //Adslot 7 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Photos_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-79289-7')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 13 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Photos_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-79289-13')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
}
// Video Watch
else if (url_dfp.search("video/watch/") != -1) {
	//Adslot 4 declaration
    gptadslots.push(googletag.defineSlot('/85406138/VideosViews_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-79289-4')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 12 declaration
    gptadslots.push(googletag.defineSlot('/85406138/videos_views_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-79289-12')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 17 declaration
    gptadslots.push(googletag.defineSlot('/85406138/VideosViews_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-79289-17')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 18 declaration
    gptadslots.push(googletag.defineSlot('/85406138/VideosViews_336x280_R2', [[336,280],[300,250]], 'div-gpt-ad-79289-18')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
}
// Video Landing
else if (url_dfp.search("/video") != -1) {
	//Adslot 3 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Videos_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-79289-3')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 9 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Videos_468x60_B1', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-79289-9')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
    //Adslot 10 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Videos_728x90_M1', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-79289-10')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
    //Adslot 11 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Videos_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-79289-11')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 16 declaration
    gptadslots.push(googletag.defineSlot('/85406138/Videos_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-79289-16')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
}
// All Other News Article
else if (url_dfp.search("/article/") != -1 || url_dfp.search("/gallery/") != -1) {

	//Adslot 3 declaration
    gptadslots.push(googletag.defineSlot('/85406138/News_Articles_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-10691-3')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 9 declaration
    gptadslots.push(googletag.defineSlot('/85406138/News_Articles_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-10691-9')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 11 declaration
    gptadslots.push(googletag.defineSlot('/85406138/News_Articles_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-10691-11')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 12 declaration
    gptadslots.push(googletag.defineSlot('/85406138/News_Articles_336x280_R2', [[336,280],[300,250]], 'div-gpt-ad-10691-12')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
	//Adslot 16 declaration
    gptadslots.push(googletag.defineSlot('/85406138/News_Articles_300x600_F1', [[300,600],[336,280],[300,250]], 'div-gpt-ad-10691-16')
                             .defineSizeMapping(map_half_page_F1)
                             .addService(googletag.pubads()));
}
// All Other News Archive Listing
else if (url_dfp.search("/article") != -1 || url_dfp.search("/gallery") != -1 || url_dfp.search("/specialsupplement-") != -1 || url_dfp.search("/topic/") != -1 || url_dfp.search("/advertise") != -1) {

	//Adslot 3 declaration
    gptadslots.push(googletag.defineSlot('/85406138/News_Articles_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-10691-3')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 9 declaration
    gptadslots.push(googletag.defineSlot('/85406138/News_Articles_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-10691-9')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 11 declaration
    gptadslots.push(googletag.defineSlot('/85406138/News_Articles_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-10691-11')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
	//Adslot 16 declaration
    gptadslots.push(googletag.defineSlot('/85406138/News_Articles_300x600_F1', [[300,600],[336,280],[300,250]], 'div-gpt-ad-10691-16')
                             .defineSizeMapping(map_half_page_F1)
                             .addService(googletag.pubads()));
}

// All Other News Sub Section
else if (url_dfp.search("/bangladesh-") != -1 || url_dfp.search("/international-") != -1 || url_dfp.search("/opinion-") != -1 || url_dfp.search("/durporobash-") != -1  || url_dfp.search("/pachmisheli") != -1   ||  url_dfp.search("/election") != -1) {

	//Adslot 2 declaration
    gptadslots.push(googletag.defineSlot('/85406138/News_Sub_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-10691-2')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 10 declaration
    gptadslots.push(googletag.defineSlot('/85406138/News_Sub_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-10691-10')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));

	//Adslot 6 declaration
    gptadslots.push(googletag.defineSlot('/85406138/News_Sub_468x60_B1', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-10691-6')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 7 declaration
    gptadslots.push(googletag.defineSlot('/85406138/News_Sub_728x90_M1', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-10691-7')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
    //Adslot 8 declaration
    gptadslots.push(googletag.defineSlot('/85406138/News_Sub_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-10691-8')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
}
// Sruti
else if(url_dfp.search("/sruti") != -1){

}
// All Other News Landing
else{

	//Adslot 1 declaration
    gptadslots.push(googletag.defineSlot('/85406138/News_728x90_T1', [[970,90],[728,90],[468,60],[320,100],[320,50]], 'div-gpt-ad-10691-1')
                             .defineSizeMapping(map_leaderboard_T1)
                             .addService(googletag.pubads()));
	//Adslot 4 declaration
    gptadslots.push(googletag.defineSlot('/85406138/News_468x60_B1', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-10691-4')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 5 declaration
    gptadslots.push(googletag.defineSlot('/85406138/News_728x90_B2', [[970,90],[728,90],[468,60],[336,280],[300,250]], 'div-gpt-ad-10691-5')
                             .defineSizeMapping(map_leaderboard_B1_B2_M1)
                             .addService(googletag.pubads()));
	//Adslot 13 declaration
    gptadslots.push(googletag.defineSlot('/85406138/News_336x280_R1', [[336,280],[300,250]], 'div-gpt-ad-10691-13')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 14 declaration
    gptadslots.push(googletag.defineSlot('/85406138/News_336x280_R2', [[336,280],[300,250]], 'div-gpt-ad-10691-14')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
    //Adslot 15 declaration
    gptadslots.push(googletag.defineSlot('/85406138/News_336x280_R3', [[336,280],[300,250]], 'div-gpt-ad-10691-15')
                             .defineSizeMapping(map_large_rectangle_R1_R2_R3)
                             .addService(googletag.pubads()));
}



    googletag.pubads().enableSingleRequest();
    googletag.pubads().collapseEmptyDivs();
    googletag.pubads().setCentering(true);

    googletag.pubads().set('adsense_ad_types', 'text_image');
    googletag.pubads().set('adsense_background_color', '#ffffff');
    googletag.pubads().set('adsense_border_color', '#ffffff');
    googletag.pubads().set('adsense_link_color', '#0000ff');
    googletag.pubads().set('adsense_text_color', '#000000');
    googletag.pubads().set('adsense_url_color', '#008000');

    googletag.enableServices();
  });
</script>
<link type="text/css" href="//www.prothomalo.com/palo-internal/paloweb-content-style.css?v=1.4" media=all rel=stylesheet />
<link type="text/css" href="//www.prothomalo.com/palo-internal/palo-modification.css?v=1.5" media=all rel=stylesheet />
<link type="text/css" href="//www.prothomalo.com/palo-internal/kiron2/Kiron.css" media=all rel=stylesheet />
<link type="text/css" href="//service.prothomalo.com/quote.css" media=all rel=stylesheet />
<style>

body{
   font-family:Kiron, SolaimanLipi, Arial, Vrinda, FallbackBengaliFont, Helvetica, sans-serif  !important ;
}
#main_menu > ul > li:first-child a {
    color: #d40909;
    text-shadow: -3px 0px 3px yellow, 3px 0px 3px yellow, 6px 0px 6px yellow, -6px 0px 6px yellow;
animation: blinker .7s linear 4 forwards;
}
@keyframes blinker {
  50% {
    opacity: 0;
  }
}
.contents .has_image.image_featured .info
{
    padding-top: 40px;
background: linear-gradient(to bottom, rgba(0,0,0,0) 0%, rgba(0,0,0,0.8) 100%);
}
.pop-main .swiper-slide .info .caption_hide{    text-shadow: 1px 1px 1px #000;}
.pop-main .pop-icons {
    text-align: right;
}
.pop-main .pop-icons .cancel {
    display: inline-block;
}
.pop-main .swiper-slide .info .caption{padding: 20px 0 12px}
.pop-each .photo a::after, a.jw_media_holder::after{background: rgb(51,51,51)}
.search_result_form {
    margin-bottom: 16px;
    background: #f6f6f6;
    padding: 16px;
}
.search_result_form .search_input {
    border: 2px solid #a8a8a8;
    background: #fff;
    height: 44px;
}
a.jw_media_holder {
    background: #F0F0ED !important;
}
.header_seach_form .search_input_holder {
    height: 48px;
    overflow: hidden;
    padding-right: 8px;
    padding: 8px;
    background: #fff;
}
.header_seach_form .search_input {
    background: #fff;
    display: block;
    border: 2px solid #f0f0ed;
    color: #000;
    height: 26px;
    line-height: 25px;
    padding: 8px 1%;
    font-size: 18px;
    font-family: SolaimanLipi;
    width: 100%;
}

.account_toggle .jw_notifications_counter.new_notification {
    color: #F44336;
    text-shadow: -2px 1px 1px #fff;
    font-weight: bold;
}
#jw_notifications .jw_notifications_counter:before {
    content: 'নোটিফিকেশন ';
    text-align: center;
}
#jw_notifications #jw_notifications_holder .each_notifications a {
    border-bottom: 0px;
    border-top: 1px solid #ccc;
    padding: 6px 16px;
}
#jw_notifications #jw_notifications_holder .status_new {
    background-color: #E3F2FD;
    color: #000;
}
#jw_notifications #jw_notifications_holder .status_old{
background-color:#fff
}
.single_album_gallery .pop-each a.pop-active::after {
    display: none;
}
.share_group_inner {
    position: absolute;
    left: -3px;
    bottom: 0;
    z-index: 1;
    background: #fff;
    box-shadow: none;
    border-radius: 3px;
    display: none;
    width: 210px;
}
.comment_share .share_group_inner{
top:0;
}
@media screen and (max-width: 1024px){
.share_group_inner {
display:block;
}
.gallery-body .share_group_inner,.comment_share .share_group_inner{display:none;}
.pop-main .share_group_inner {
display:none;
}
.gallery-body .share_group_inner{
left:33px;
}
.pop-main .share_group:hover .share_group_inner {
    display: block;
    bottom: 46px;
left:-16px;
}
.pop-main .share_group:hover .share_group_inner:after {
    content: '';

    border-top: 10px solid #fff;
    border-left: 10px solid transparent;
    border-right: 10px solid transparent;
    position: absolute;
    bottom: -10px;
    left: 21px;
}
}
@media screen and (min-width: 801px){

.comments_holder .share_group:hover .share_group_inner {
    padding: 8px;
    width: 320px;
    box-shadow: none;
    height: 38px;
    background: transparent;
    top: -10px;
    left: 24px;
}
body.no-scrollbar .main_menu{
	display:none;
}
.more_main_menu_wrap{
	top:64px;
}
.more_main_menu_inner {
    background: #fff;
    padding: 1px 5%;
    top:0;
}
.top_big_menu {
    border-top: 1px solid #ccc;
    max-width: 1280px;
    margin: auto;
}
.big_menu .big_menu_top{
    border-bottom: 1px solid #ccc;
    padding: 24px 0;
}
.big_menu .big_menu_bottom{    padding-top: 24px;}
.big_menu .big_menu_top .special_menu ul li a{    line-height: 40px;}
.big_menu .big_menu_bottom .bmenu_bottom_toplinks{    margin-bottom: 24px;}
.close_more_main{display:none}

.big_menu .big_menu_bottom .bmenu_bottom_imagelinks {
    margin-bottom: 24px;
}
.foot-middle-container{padding-bottom:0}
.big_menu  .big_menu_bottom .bmenu_bottom_right{padding-bottom:24px}
.big_menu .big_menu_bottom .bmenu_bottom_right p {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 14px;
    line-height: 20px;
    font-weight: normal;
}
.foot_big_menu.big_menu .big_menu_top{    border-bottom: 1px solid #4a4a4a;}
.office_address{
    float: left;
    margin-right: 4px;
}
/* end menu fix */
.more_main_menu_wrap{overflow: hidden;}
body.no-scrollbar{overflow-y: scroll !important;padding-top: 64px !important;}

.header_social_wrap{
    position:relative;
}
.header_social_wrap .social_links {
    display: none;
    position: absolute;
    top: 76%;
    right: 0;
    background: transparent;
    z-index: 5;
    box-shadow:none;
}
.social_links.click-free-pop-active:before {
    content: '';
    border-top: 15px solid #fff;
    border-left: 0px solid transparent;
    border-right: 16px solid transparent;
    position: absolute;
    right: 0;
    height: 0px;
    background: #f1f1f1;
    width: 93%;
}
.header_social_wrap .social_links ul {
    list-style: none;
    background: #ffffff;
    box-shadow: 0 0 5px #000;
    margin-top: 15px;
}
.header_social_wrap .social_links a {
    color: #616161;
    display: block;
    overflow: hidden;
    padding: 6px 16px;
    display:inline-flex;
    min-width: 106px;
}
.header_social_wrap .social_links a:before {
    font-family: font-jade;
    margin-right: 4px;
    float: left;
    width: 20px;
}
#jw_notifications #jw_notifications_holder {
    position: relative;
    width: auto;
    box-shadow: none;
	top:0;
}
#account_bar .profile_link {
    padding-left: 16px;
}
#account_bar .profile_link, #account_bar .logout_link {
    border-right: 0 none;
}
#account_bar a {
    float: none;
    padding: 6px 16px;
    text-decoration: none;
    display: block;
    border-bottom: 1px solid #ccc;
}
#account_bar .profile_pic {
    margin-right: 8px;
    height: 32px;
    float: left;
}
#jw_notifications {
    position: relative;
    float: none;
}
#jw_notifications .jw_notifications_counter {
    background: transparent;
    box-shadow: none;
    border: 0 none;
    padding: 6px 16px;
    float: none;
}
i.demo-icon.icon-off {
    font-size: 22px;
}
.icon-off:before {
    margin: 0 14px 0 0;
}
.header_account_wrap {
    position: relative;
}
.user_account{
    min-width: 250px;
    top:48px;
}
.user_account.click-free-pop-active:before {
    content: '';
    border-top: 16px solid #fff;
    background: #f1f1f1;
    position: absolute;
    right: 0;
    border-left: 0 solid transparent;
    border-right: 16px solid transparent;
    height: 0px;
}
#account_bar{
    margin-top:16px;
    box-shadow: 0px 5px 5px rgba(0, 0, 0, 0.35);
width: 100%;
}
}
.header_seach_form .search_input_holder {
    height: 48px;
    overflow: hidden;
    padding-right: 8px;
    padding: 8px;
    background: #fff;
}
.header_seach_form .search_input {
    background: #fff;
    display: block;
    border: 2px solid #f0f0ed;
    color: #000;
    height: 26px;
    line-height: 25px;
    padding: 8px 1%;
    font-size: 18px;
    font-family: SolaimanLipi;
    width: 100%;
}
.header_seach_form .search_close {
    width: 64px;
    height: 46px;
    line-height: 46px;
    float: right;
    text-align: center;
    cursor: pointer;
    background: #efefef;
    margin-top: 8px;
}
.header_seach_form .search_button {
    float: right;
    height: 46px;
    line-height: 46px;
    color: #000;
    background: #efefef;
    width: 64px;
    border: 0 none;
    cursor: pointer;
    border-right: 1px solid #fff;
    border-left: 1px solid #f0f0f0;
    margin-top: 8px;
}
.video_summery.content {
    display: none;
}

.footer_only_mobile .bottom{display: none}
@media screen and (max-width: 800px){

.footer_only_mobile .bottom{display: block; margin-bottom: 24px;}
.footer_only_mobile .bottom a.more_link{
    color: #369;
    font-size: 16px;
    background-color: #f0f0ed;
    padding: 12px 32px;
    line-height: normal;
    display: block;
    border-radius: 0;
    border-bottom: 1px solid #9eb6ce;
}

.palo_break{display:block;}
.pop-each .photo a.pop-active::after, a.jw_media_holder.pop-active::after{display:none}
.pop-main .pop-slide {
    position: relative;
    height: 100% !important;
}
.pop-main .pop-thumb {
    position: absolute;
    bottom: 0;
    display: none;
}
.comments_holder .share_group:hover .share_group_inner {
    box-shadow: none;
    left: 24px;
    top: -10px;
}
.search_result_form{padding:8px}
.search_result_form .select_holder {
    float: left;
    margin-right: 0;
    border-bottom: 1px solid #ccc;
    padding: 8px 1%;
    width: 98%;
}
.big_menu .big_menu_top .special_menu ul li{margin-right:36px}
.big_menu .big_menu_bottom .bmenu_bottom_imagelinks ul li a span {
    display: block;
    height: 32px;
    line-height: 32px;
    margin-right: 12px;
    float: left;
    width: 32px;
    text-align: center;
}
a[title="Print"].jadeshare{
display:none;
}
.share_group_inner{width:241px;}
.secondary_menu_toggle{top:30px}
.has_sub{height:56px;margin-bottom:38px}
.secondary_logo .subpage_logo {
    font-size: 24px;
    line-height: 30px;
    clear: both;
    float: none;
    width: 94%;
    position: absolute;
    margin-top: 10px;
    padding: 0 1%;
display:block;
}
.secondary_logo .subpage_logo:before {
    border-left: 4px solid #d84315;
    content: '';
    font-size: 18px;
    padding-right: 4px;
}
.secondary_menu_wrap {
    width: 66%;
    right: 0;
    left: 32%;
    top: 47px;
    box-shadow: 0px 4px 5px #000;
}

.secondary_menu a:hover, .secondary_menu a.active, .secondary_menu ul li:last-child a.active {
    border-left: 4px solid #c00;
    text-decoration: none;
    padding-left: 12px;
border-bottom: 1px solid #eaeaea;
}
.secondary_menu a {
    border-bottom: 1px solid #eaeaea;
}
.secondary_menu_toggle.opened{background-color: #fff}
.header_seach_form .search_button, .header_seach_form .search_close {
    width: 55px;
    height: 46px;
    line-height: 46px;
    margin-top: 8px;
}
.header_seach_form form[id^=jadewits_search_form]{
	background-color: #fff;
    padding-right: 8px;
    box-shadow: 0 8px 8px -8px #000;
}
.header_social_wrap .social_links {
    top: 110px;
    left: 0;
    box-shadow: none;
    background: #fff;
    padding: 12px 1%;
    box-shadow: 0 5px 5px -5px #000;
}
.mh_toggle {
    position: static;
}
.header_social_wrap .social_links ul {
    float: right;
}
.header_social_wrap .social_links li {
    border-bottom: 0 none;
	float: left;
}
.header_social_wrap .social_links a {
    padding: 0;
    width: 32px;
    height: 32px;
    margin-right: 12px;
    border-radius: 16px;
}
.social_links a.facebook:before {
	color: #fff !important;
    background-color: #4267a5;
    padding: 8px 11px;
}
.social_links a.twitter:before {
    background-color: #1da1f2;
    padding: 8px;
    color: #fff !important;
}
.social_links a.pinterest:before {
    background-color: #bd081c;
    padding: 8px 10px;
    color: #fff !important;
}
.social_links a.googleplus:before {
    background-color: #dc4a38;
    padding: 8px 4px;
    color: #fff !important;
}
.social_links a.linkedin:before {
    background-color: #0078ba;
    padding: 8px;
    color: #fff !important;
}
.social_links a.instagram:before {
    background-color: #6b3ccb;
    padding: 8px 6px;
    color: #fff !important;
}
.account_toggle:before{
    font-size: 22px;
    line-height: 30px;
}
.user_account {
    width: 98%;
    top: 110px;
    left: 0;
    background-color: #fff;
    padding: 12px 1%;
    box-shadow: 0 5px 5px -5px #000;
}
#account_bar {
    background: transparent;
    box-shadow: none;
}
#jw_notifications .jw_notifications_counter {
    box-shadow: none;
    background: transparent;
}
.social_toggle, .account_toggle:before, .account_toggle, .account_toggle .profile_link_holder, .account_toggle .profile_link_holder img{
	width:32px;
	height:32px;
}
.social_toggle:before {
    font-size: 22px;
    line-height: 30px;
    width: 32px;
    height: 32px;
}
.account_toggle:before, .social_toggle:before{
	margin-top: 14px;
}
.header_account_wrap {
    margin-right: 16px;
}
.other_language_link{line-height:60px}
#account_bar a + a {
    border-left: 1px solid #ccc;
}
.comments_title{
padding: 24px 16px 8px;
    margin: 12px -16px;
    background-color: #e2e2e2;
    box-shadow: 0px 8px 8px -8px #9a9a9a inset;
}
.comments_holder .share_group .share_group_inner {
    display: none;
}
.comments_holder .share_group:hover .share_group_inner{
    display: block;
}

}
li.menu_page_id_1401 a {
    color: #ff7a00;
}
</style>
<style>
/*featured part style*/
.palo_featured_1 .has_image h2.title_holder {
    font-size: 30px;
    line-height: 40px;
}

/* Today's paper Rounak */


.todays_newspaper_pages_widget .todayspaper_container li.headbar:before {    
    height: 18px;    
    margin-top: 7px;
}


/* Tabbed widget footer hide Rounak 
.contents_tabbed .view_all_wrap{
display: none;
}
.contents_tabbed  .tabbed_conents .tabs_content ul li:last-child{
border-bottom: none;
}
*/
/* start todays paper menu*/

 .palo_todays_paper_widget .todayspaper_container{
	background-color:  #f6f6f6;
	position: relative;
}
.palo_todays_paper_widget .todayspaper_container h3{
	padding: 16px;
	border-bottom: 1px solid #e7e7e7;
	color: #555555;
	font-size: 18px;
	margin-bottom: 0px;
	margin-top: 0px;	

}

.palo_todays_paper_widget ul.menu_container_t{
	padding: 16px 0px 25px 16px;
	margin: 0px;
}
.palo_todays_paper_widget ul.menu_container_t  li{	
	font-size: 16px;
	list-style: none;
	margin: 0;
	padding: 5px 0px;

}
.palo_todays_paper_widget ul.menu_container_t li a{
	color: #999999;
	text-decoration: none;
}
.palo_todays_paper_widget ul.menu_container_t li a:hover{
	color: #333333;	
	text-decoration: none;	
}

.palo_todays_paper_widget li.headbar:before {
    content: ' ';
    width: 4px;
    height: 20px;    
    background: #c00;
}
.palo_todays_paper_widget ul.menu_container_t li.headbar a{
	padding-left: 10px;
	color: #000;
	cursor: auto;
	font-size: 18px;
}
.palo_todays_paper_widget  .secondary_menu_wrap_palo {
    height: auto;
    background: none;   
}
.palo_todays_paper_widget  .secondary_menu_palo li, .palo_todays_paper_widget  .secondary_menu_palo a {
    float: none;
}

.palo_todays_paper_widget  .secondary_menu_palo a:hover, .palo_todays_paper_widget  .secondary_menu_palo a.active {
    border-bottom: none;    
}

.palo_todays_paper_widget .todayspaper_container li.headbar:before {
    height: 18px;
    margin-top: 7px;
}
.bottom, .pagination {
    text-align: center;
}

.bottom a.more_link, .pagination .next_page, .pagination .previous_page{
    background-color: #757575;
    padding: 12px 90px;
    color: #ffffff;
    font-size: 20px;
    border-radius: 4px;
}

.pagination .next_page, .pagination .previous_page{
    float:none;
    padding: 12px 40px;
}
.mobile_show{
display: none;
margin:auto;
}
.desktop_show {
    display: block;
	margin: 0px auto 16px;
}
.news_inner_spcl_ad {
    float: left;
    margin-right: 15px;
}
span.highlighted_txt {
    color: #054e84;
    font-weight: bold;    
}

/*
.section_footer.widget a.more_link {
    color: #231f20;
    background-color: #a0a0a0;
    font-size: 20px;
    line-height: 28px;
    padding: 6px;
   
}
.pagination a, .pagination span {
    color: #FFFFFF !important;
}
*/
 @media screen and (max-width: 800px) {
	 .desktop_show {
    display: none;
}
.mobile_show{
display: block;
margin: 4px auto 10px;
}
.news_inner_spcl_ad {
    float: none;
    text-align: center;
   margin-right: 0px;
}
.bottom a.more_link, .section_footer.widget a.more_link{
   line-height: 70px;
}
.pagination .next_page, .pagination .previous_page{
line-height: 20px;
}

.contents .has_image.m_show_image_as_top .info h2.title_holder .title{
font-size:22px;
line-height:30px;
}
.contents .has_image.image_left .info h2.title_holder .title, .contents.m_show_2col .has_image.m_show_image_as_top .info h2.title_holder .title{
font-size:18px;
line-height:24px;
}

.palo_todays_paper_widget  .secondary_menu_wrap_palo {
   
    box-shadow: 0px 4px 5px #000;
    height: auto;
    position: absolute;    
    z-index: 4;
    background: #fff;
    width: 50%;   
    top: 0px;    
    left: 50%;
display:none;
}

.section_footer.widget a.more_link {
    margin: 10PX;
}
.secondary_menu_toggle_palo.opened::before {
    font-family: font-jade;
    font-size: 24px;
}

.secondary_menu_toggle_palo {
    position: absolute;

  /*  top: 50%;
  right: 10px;*/
   top: 20px;
    right: 3px;
    margin-top: -17px;
    height: 34px;
    width: 34px;
    text-align: center;
    line-height: 34px;
    background: rgba(0,0,0, 0.15);
    color: #000;
    cursor: pointer;
}

.todayspaper_container {
line-height: 0px;
}
.calender_icon {
 float: left;
 margin-left: 20px;
}
.palo_todays_paper_widget ul.menu_container_t {
 padding: 0;
 display: block;
background: #fff;
}
 
.palo_todays_paper_widget  ul.menu_container_t li.headbar {
    background: none;
    box-shadow: none;
}
.palo_todays_paper_widget li.headbar:before {
 content: ' ';
 width: 0;
 height:;

 background: none;
 padding-right: 0px;
}
 
 .mobile_button {
 background-color: #f6f6f6;
}
.todays_newspaper_pages_widget  ul.menu_container_t li {    
    padding: 0px 0px;
}
.palo_todays_paper_widget  ul.menu_container_t li a{    
   color: #000;
}
.palo_todays_paper_widget  ul.menu_container_t li.headbar a {
    border-left: 4px solid #c00;
    text-decoration: none;
    padding-left: 12px;
    border-bottom: 1px solid #eaeaea;
}

.secondary_menu_palo a {
    line-height: 44px;
    padding: 0 10px;
    font-size: 16px;
    border-bottom: 0 none;
    color: #000;
   border-bottom: 1px solid #eaeaea;
   display:block;
}

}
.palo_privacy_link{color: #999999 !important; text-decoration: underline;}
.palo_privacy_link:hover{color: #ffffff;}


/* end todays paper menu*/
</style>
<script>
  var _comscore = _comscore || [];
  _comscore.push({ c1: "2", c2: "20420819" });
  (function() {
    var s = document.createElement("script"), el = document.getElementsByTagName("script")[0]; s.async = true;
    s.src = (document.location.protocol == "https:" ? "https://sb" : "https://b") + ".scorecardresearch.com/beacon.js";
    el.parentNode.insertBefore(s, el);
  })();
</script>
<noscript>
<img src="https://b.scorecardresearch.com/p?c1=2&c2=20420819&cv=2.0&cj=1"/>
</noscript>
<script>

_atrk_opts = { atrk_acct:"VTJem1aIF5R1fn", domain:"prothomalo.com",dynamic: true};

(function() { var as = document.createElement('script'); as.type = 'text/javascript'; as.async = true; as.src = "https://certify-js.alexametrics.com/atrk.js"; var s = document.getElementsByTagName('script')[0];s.parentNode.insertBefore(as, s); })();

</script>
<noscript><img src="https://certify.alexametrics.com/atrk.gif?account=VTJem1aIF5R1fn" style=display:none height=1 width=1 alt=""/></noscript>
<meta name=google-site-verification content=uRs2Ls-3fpuKgaEKAvA2VyjiZV3lPAQiKnRl9wpxsVA />
</head>
<body class="page_color_ jw_body_page_id_102 jw_body_content_id_1574390 ">
<div id=fb-root></div>
<script>(function(d, s, id) {
 var js, fjs = d.getElementsByTagName(s)[0];
 if (d.getElementById(id)) return;
 js = d.createElement(s); js.id = id;
 js.src = "//connect.facebook.net/en_US/sdk.js#xfbml=1&version=v2.7&appId=1499138263726489";
 fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));</script>
<div class=whole_wrapper>
<div class=whole_inner>
<div class="header_wrap ">
<div class=header>
<h2 class=site_logo>
<a href="/"><img height=46 src="//paloimages.prothom-alo.com/contents/themes/public/style/images/Prothom-Alo.png" alt="প্রথম আলো"/></a>
</h2>
<div class=header_right_part>
<div class=header_right_inner>
<span class=more_main_menu><span>সব</span></span>
<div class=more_main_menu_wrap>
<div class=more_main_menu_inner>
<span class=close_more_main></span>
<div class="top_big_menu big_menu">
<div class=big_menu_top>
<div class=all-menu>
<ul id=13><li class="menu_page_id_37 menu_color_"><a class="static " href="/home">প্রচ্ছদ</a></li><li class="menu_page_id_ menu_color_"><a class=" " href="https://election.prothomalo.com/?utm_source=Prothomalo&utm_medium=Home%20Menu&utm_campaign=Ban-WI_Nov-18&utm_term=National_Election2018_Home_Menu" target=_blank>নির্বাচন ২০১৮</a></li><li class="menu_page_id_102 menu_color_"><a class="dynamic " href="/bangladesh">বাংলাদেশ</a></li><li class="menu_page_id_153 menu_color_"><a class="dynamic " href="/international">আন্তর্জাতিক</a></li><li class="menu_page_id_189 menu_color_"><a class="dynamic " href="/economy">অর্থনীতি</a></li><li class="menu_page_id_246 menu_color_"><a class="dynamic " href="/opinion">মতামত</a></li><li class="menu_page_id_216 menu_color_"><a class="dynamic " href="/sports">খেলা</a></li><li class="menu_page_id_390 menu_color_"><a class="dynamic " href="/entertainment">বিনোদন</a></li><li class="menu_page_id_1051 menu_color_"><a class="dynamic " href="/cartoon">কার্টুন</a></li><li class="menu_page_id_474 menu_color_"><a class="static " href="/features">ফিচার</a></li><li class="menu_page_id_324 menu_color_"><a class="dynamic " href="/technology">বিজ্ঞান ও প্রযুক্তি</a></li><li class="menu_page_id_285 menu_color_"><a class="dynamic " href="/life-style">জীবনযাপন</a></li><li class="menu_page_id_363 menu_color_"><a class="dynamic " href="/education">শিক্ষা</a></li><li class="menu_page_id_463 menu_color_"><a class="dynamic " href="/onnoalo">শিল্প ও সাহিত্য</a></li><li class="menu_page_id_438 menu_color_"><a class="dynamic " href="/we-are">আমরা</a></li><li class="menu_page_id_493 menu_color_"><a class="dynamic " href="/pachmisheli">পাঁচমিশালি</a></li><li class="menu_page_id_504 menu_color_"><a class="dynamic " href="/special-supplement">বিশেষ সংখ্যা</a></li><li class="menu_page_id_536 menu_color_"><a class="dynamic " href="/northamerica" target=_blank>উত্তর আমেরিকা</a></li><li class="menu_page_id_ menu_color_"><a class=" " href="https://epaper.prothomalo.com/" target=_blank>ইপেপার</a></li></ul>	</div>
<script>
													  jw_menu_fixer('.footer_menu','navigation');
												 </script>
<div class=special_menu>
<ul>
<li><a class=image_menu_icon href="/photo">ছবি</a></li>
<li><a class=video_menu_icon href="/video">ভিডিও</a></li>
<li><a class=archive_menu_icon href="/archive">আর্কাইভ</a></li>
</ul>
</div>
</div>
<div class=big_menu_bottom>
<div class=bmenu_bottom_left>
<div class=bmenu_bottom_toplinks>
<ul id=6><li class="menu_page_id_540 menu_color_"><a class="static " href="/advertise" target=_blank>বিজ্ঞাপন</a></li><li class="menu_page_id_544 menu_color_"><a class="static " href="/circulation" target=_blank>সার্কুলেশন</a></li><li class="menu_page_id_820 menu_color_"><a class="static " href="/hajj" target=_blank>পবিত্র হজ</a></li><li class="menu_page_id_736 menu_color_"><a class="dynamic archive" href="/durporobash" target=_blank>দূর পরবাস</a></li><li class="menu_page_id_536 menu_color_"><a class="dynamic " href="/northamerica" target=_blank>উত্তর আমেরিকা</a></li></ul>	</div>
<script>
											jw_menu_fixer('.footer_menu','navigation');
										</script>
<div class=bmenu_bottom_imagelinks>
<ul>
<li><a href="https://www.prothomalo.com/22221" target=_blank><span><img src="https://paloimages.prothom-alo.com/contents/themes/public/style/images/2221_icon.png" alt=""/></span>২২২২১</a></li>
<li><a href="https://www.prothomalo.com/trust" target=_blank><span><img src="https://paloimages.prothom-alo.com/contents/themes/public/style/images/trust_icon.png" alt=""/></span>ট্রাস্ট</a></li>
<li><a href="https://www.prothomalo.com/protichinta" target=_blank><span><img src="https://paloimages.prothom-alo.com/contents/themes/public/style/images/pchinta_icon.png" alt=""/></span>প্রতিচিন্তা</a></li>
<li><a href="https://www.prothomalo.com/kishoralo" target=_blank><span><img src="https://paloimages.prothom-alo.com/contents/cache/images/32X27X1/uploads/media/2018/09/24/e483aba8dfa8077ce2cb0b8e2429cc63-5ba8829143ed0.png" alt="কিশোর আলো"/></span>কিশোর আলো</a></li>
<li><a href="https://bit.ly/1yJDU9O" target=_blank rel=nofollow><span><img src="https://paloimages.prothom-alo.com/contents/themes/public/style/images/abcradio_icon.png" alt=""/></span>abc রেডিও</a></li>
<li><a href="https://www.prothomalo.com/bondhushava" target=_blank><span><img src="https://paloimages.prothom-alo.com/contents/cache/images/87x32x1/cache/uploads/media/2018/08/14/331e6cfb410b31c8288e18745ac83e24-5b72068060ea9.png" alt=""/></span></a></li>
</ul>	</div>
</div>
</div>
</div>
</div>
</div>
<script>
								$('.more_main_menu').click(function(){ 
									$('.more_main_menu_wrap').toggle(200); 
									$('body').toggleClass('no-scrollbar');
									$('.more_main_menu').toggleClass('opened');
									$('.mh_toggle').toggleClass('db');
									});
								$('.close_more_main').click(function(){
									$('.more_main_menu_wrap').toggle(200);
									$('body').toggleClass('no-scrollbar');
									$('.more_main_menu').toggleClass('opened');
									$('.mh_toggle').toggleClass('db');
									});
								$('.more_main_menu_wrap' ).click(function(e){
									if(e.target !== e.currentTarget) return;
									$('.more_main_menu_wrap').toggle(200);
									$('body').toggleClass('no-scrollbar');
									$('.more_main_menu').toggleClass('opened');
									$('.mh_toggle').toggleClass('db');
								});
							</script>
<div class="other_language_link mh_toggle">
<a target=_blank href="http://en.prothomalo.com/">English</a>
</div>
<div class="header_account_wrap mh_toggle">
<span class="account_toggle  click-free-pop" data-pop=.user_account>
<span class=profile_link_holder></span>
<span class=jw_notifications_counter></span>
</span>
<div class=user_account>
<div id=account_bar>
<a class=login_link id=_jadewits_login href="https://profiles.prothomalo.com/login/?APP_ID=1&next=https%3A%2F%2Fwww.prothomalo.com%2Fbangladesh%2Farticle%2F1574390%2F%25E0%25A6%25B8%25E0%25A7%2581%25E0%25A6%25AC%25E0%25A6%25B0%25E0%25A7%258D%25E0%25A6%25A3%25E0%25A6%259A%25E0%25A6%25B0%25E0%25A7%2587-%25E0%25A6%25A7%25E0%25A6%25B0%25E0%25A7%258D%25E0%25A6%25B7%25E0%25A6%25A3%25E0%25A7%2587%25E0%25A6%25B0-%25E0%25A6%2598%25E0%25A6%259F%25E0%25A6%25A8%25E0%25A6%25BE%25E0%25A6%25B0-%25E0%25A6%25B8%25E0%25A6%2599%25E0%25A7%258D%25E0%25A6%2597%25E0%25A7%2587-%25E0%25A6%25AD%25E0%25A7%258B%25E0%25A6%259F%25E0%25A7%2587%25E0%25A6%25B0-%25E0%25A6%25B8%25E0%25A6%25AE%25E0%25A7%258D%25E0%25A6%25AA%25E0%25A6%25B0%25E0%25A7%258D%25E0%25A6%2595-%25E0%25A6%25AA%25E0%25A6%25BE%25E0%25A7%259F%25E0%25A6%25A8%25E0%25A6%25BF">লগইন</a>
<a class=register_link id=_jadewits_register href="https://profiles.prothomalo.com/register/?APP_ID=1&next=https%3A%2F%2Fwww.prothomalo.com%2Fbangladesh%2Farticle%2F1574390%2F%25E0%25A6%25B8%25E0%25A7%2581%25E0%25A6%25AC%25E0%25A6%25B0%25E0%25A7%258D%25E0%25A6%25A3%25E0%25A6%259A%25E0%25A6%25B0%25E0%25A7%2587-%25E0%25A6%25A7%25E0%25A6%25B0%25E0%25A7%258D%25E0%25A6%25B7%25E0%25A6%25A3%25E0%25A7%2587%25E0%25A6%25B0-%25E0%25A6%2598%25E0%25A6%259F%25E0%25A6%25A8%25E0%25A6%25BE%25E0%25A6%25B0-%25E0%25A6%25B8%25E0%25A6%2599%25E0%25A7%258D%25E0%25A6%2597%25E0%25A7%2587-%25E0%25A6%25AD%25E0%25A7%258B%25E0%25A6%259F%25E0%25A7%2587%25E0%25A6%25B0-%25E0%25A6%25B8%25E0%25A6%25AE%25E0%25A7%258D%25E0%25A6%25AA%25E0%25A6%25B0%25E0%25A7%258D%25E0%25A6%2595-%25E0%25A6%25AA%25E0%25A6%25BE%25E0%25A7%259F%25E0%25A6%25A8%25E0%25A6%25BF">রেজিস্টার</a>
</div>
<script>
									if( __user_login_check ){				
										document.write('<' + 'script type="text/javascript" src="https://profiles.prothomalo.com/api/authentication_helper/account_bar/?contianer=account_bar&APP_ID=1&amp;_hl=bn"></' + 'script>');
										}
									</script>
</div>
</div>
<div class=header_search_wrap>
<span class="search_toggle click-free-pop" data-pop=.header_seach_form></span>
<div class=header_seach_form>
<form id=jadewits_search_form_1223 action="/search/">
<span class=search_close></span>
<button class=search_button type=submit><span>অনুসন্ধান</span></button>
<div class=search_input_holder>
<input class="search_input jadewits_keyboard " name=q data-keyboardfixedpos=32 value="" placeholder="কী খুঁজতে চান?">
</div>
</form>
<script>
										$('#jadewits_search_form_1223').submit(function(){
											var search_text = $.trim($('[name=q]',this).val());
											if( search_text == 'কী খুঁজতে চান?' || !search_text){
												alert('Please type something to search');
												return false;
												}
											return true;
											});
									</script>
</div>
<script>$('.search_toggle').click(function(){  /*$('.header_seach_form .search_input').focus();*/});$('.header_seach_form  .search_close').click(function(){ $('.header_seach_form').toggle();});
								
								/*$('.header_seach_form .search_input').focus(function(){
									$('#banglaInpTool').addClass('keyboard_top');
									});
								$('.header_seach_form .search_input').blur(function(){
									$('#banglaInpTool').removeClass('keyboard_top');
									});*/
								
								</script>
</div>
<div class="header_social_wrap mh_toggle">
<span class="social_toggle click-free-pop" data-pop=.social_links></span>
<div class=social_links>
<ul>
<li><a rel=nofollow target=_blank class=facebook href="https://www.facebook.com/DailyProthomAlo"><span>Facebook</span></a></li>	<li><a rel=nofollow target=_blank class=twitter href="https://twitter.com/ProthomAlo"><span>Twitter</span></a></li>	<li><a rel=nofollow target=_blank class=pinterest href="https://www.pinterest.com/ProthomAlo"><span>Pinterest</span></a></li>
<li><a rel=nofollow target=_blank class=googleplus href="https://plus.google.com/+ProthomAlo"><span>Google Plus</span></a></li>
<li><a rel=nofollow target=_blank class=youtube href="https://www.youtube.com/c/ProthomAlo"><span>YouTube</span></a></li>	<li><a rel=nofollow target=_blank class=instagram href="https://www.instagram.com/prothomalo/"><span>Instagram</span></a></li>	</ul>
</div>
</div>
</div>
</div>
<div class=header_menu_wrap>
<span class=main_menu_toggle></span>
<div id=main_menu class=main_menu>
<ul id=9><li class="menu_page_id_ menu_color_"><a class=" " href="https://election.prothomalo.com/?utm_source=Prothomalo&utm_medium=Home_Menu&utm_campaign=National_Election-18_Home_Menu" target=_blank>নির্বাচন ২০১৮</a></li><li class="menu_page_id_102 menu_color_"><a class="dynamic " href="/bangladesh">বাংলাদেশ</a></li><li class="menu_page_id_153 menu_color_"><a class="dynamic " href="/international">আন্তর্জাতিক</a></li><li class="menu_page_id_189 menu_color_"><a class="dynamic " href="/economy">অর্থনীতি</a></li><li class="menu_page_id_246 menu_color_"><a class="dynamic " href="/opinion">মতামত</a></li><li class="menu_page_id_216 menu_color_"><a class="dynamic " href="/sports">খেলা</a></li><li class="menu_page_id_390 menu_color_"><a class="dynamic " href="/entertainment">বিনোদন</a></li><li class="menu_page_id_475 menu_color_"><a class="dynamic " href="/photo">ছবি</a></li><li class="menu_page_id_498 menu_color_"><a class="dynamic " href="/video">ভিডিও</a></li><li class="menu_page_id_ menu_color_"><a class=" " href="https://epaper.prothomalo.com/" target=_blank>ইপেপার</a></li><li class="menu_page_id_536 menu_color_"><a class="dynamic " href="/northamerica" target=_blank>উত্তর আমেরিকা</a></li><li class="menu_page_id_285 menu_color_"><a class="dynamic " href="/life-style">জীবনযাপন</a></li></ul>	</div>
<script>
							jw_menu_fixer('.main_menu','navigation');
							//now run horizontal menu hover helper
							//jadewits_horizontal_hover_menu({container:'.main_menu',waittime:500});
						</script>
</div>
</div>
</div>
<div class=secondary_header style="
				
								
									background-image:url('//paloimages.prothom-alo.com/contents/uploads/default/2017/01/22/27ab23e0abfef085995032b4037b236e-58843f438f52d.png');
								
					background-position:top center;
					background-repeat:no-repeat;
					-webkit-background-size: cover;
					-moz-background-size: cover;
					-o-background-size: cover;
					background-size: cover;
				">
<div class=secondary_top>
<div class=container>
<h2 class=secondary_logo>
<a href="/bangladesh">
<span>বাংলাদেশ</span>
</a>
</h2>
</div>
</div>
<span class="secondary_menu_toggle "></span>
<div class=secondary_menu_wrap>
<div class=container>
<div id=secondary_menu class=secondary_menu>
<ul id=12><li class="menu_page_id_577 menu_color_"><a class="static " href="/election">নির্বাচন</a></li><li class="menu_page_id_825 menu_color_"><a class="static " href="/bangladesh-divisions">বিভাগ</a></li><li class="menu_page_id_105 menu_color_"><a class="static " href="/bangladesh-politics">রাজনীতি</a></li><li class="menu_page_id_497 menu_color_"><a class="static " href="/bangladesh-government">সরকার</a></li><li class="menu_page_id_108 menu_color_"><a class="static " href="/bangladesh-crime">অপরাধ</a></li><li class="menu_page_id_111 menu_color_"><a class="static " href="/bangladesh-justice">আইন ও বিচার</a></li><li class="menu_page_id_114 menu_color_"><a class="static " href="/bangladesh-environment">পরিবেশ</a></li><li class="menu_page_id_499 menu_color_"><a class="static " href="/bangladesh-accident">দুর্ঘটনা</a></li><li class="menu_page_id_500 menu_color_"><a class="static " href="/bangladesh-parliament">সংসদ</a></li><li class="menu_page_id_120 menu_color_"><a class="static " href="/bangladesh-capitalcity">রাজধানী</a></li><li class="menu_page_id_117 menu_color_"><a class="static " href="/bangladesh-population">জনসংখ্যা</a></li><li class="menu_page_id_150 menu_color_"><a class="static " href="/bangladesh-others">বিবিধ</a></li></ul>	</div>
</div>
</div>
<script>
						jw_menu_fixer('.secondary_menu','navigation');
						$('.secondary_menu_toggle').click(function(){ 
							$('.secondary_menu_wrap').toggle();
							$('.secondary_menu_toggle').toggleClass('opened');
							});
						//now run horizontal menu hover helper
						//jadewits_horizontal_hover_menu({container:'.main_menu',waittime:500});
					</script>
</div>
<div class="spacer mb24"></div>
<div class="header_ad_block advertisement"><script>
// Homepage Archive
if (url_dfp.search("/home/") != -1 || url_dfp.search("/archive") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Home_728x90_T1' -"+"-><div id='div-gpt-ad-44697-1'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-44697-1'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// Sports Details Article / Gallery
else if (url_dfp.search("sports/article/") != -1 || url_dfp.search("sports/gallery/") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Sports_Articles_728x90_T1' -"+"-><div id='div-gpt-ad-19259-3'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-19259-3'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// Sports Archive / Listing
else if (url_dfp.search("sports/article") != -1 || url_dfp.search("sports/gallery") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Sports_Articles_728x90_T1' -"+"-><div id='div-gpt-ad-19259-3'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-19259-3'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
	// Fixture page Landing
else if(url_dfp.search("/sports-fixture") != -1){

}
// Live Score Sports
else if (url_dfp.search("/sports-results") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Sports_Live_Scores_T1' -"+"-><div id='div-gpt-ad-19259-4'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-19259-4'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// Sports Sub Section
else if (url_dfp.search("/sports-") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Sports_Sub_728x90_T1' -"+"-><div id='div-gpt-ad-19259-2'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-19259-2'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// Sports Landing
else if (url_dfp.search("/sports") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Sports_728x90_T1' -"+"-><div id='div-gpt-ad-19259-1'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-19259-1'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// Sports Landing
else if (url_dfp.search("/fifa-world-cup") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Sports_728x90_T1' -"+"-><div id='div-gpt-ad-19259-1'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-19259-1'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}

else if (url_dfp.search("/asia-cup") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Sports_728x90_T1' -"+"-><div id='div-gpt-ad-19259-1'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-19259-1'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// Technology Details Article / Gallery
else if (url_dfp.search("technology/article/") != -1 || url_dfp.search("technology/gallery/") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Tech_Articles_728x90_T1' -"+"-><div id='div-gpt-ad-34418-3'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-34418-3'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// Technology Archive / Listing
else if (url_dfp.search("technology/article") != -1 || url_dfp.search("technology/gallery") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Tech_Articles_728x90_T1' -"+"-><div id='div-gpt-ad-34418-3'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-34418-3'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// Technology Sub-category
else if (url_dfp.search("/technology-") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Tech_Sub_728x90_T1' -"+"-><div id='div-gpt-ad-34418-2'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-34418-2'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// Technology Landing
else if (url_dfp.search("/technology") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Technology_728x90_T1' -"+"-><div id='div-gpt-ad-34418-1'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-34418-1'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}



// bondhushava Details Article / Gallery
else if (url_dfp.search("bondhushava/article/") != -1 || url_dfp.search("bondhushava/gallery/") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Bondhushava_Articles_728x90_T1' -"+"-><div id='div-gpt-ad-5720320-2'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-5720320-2'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// bondhushava Archive / Listing
else if (url_dfp.search("bondhushava/article") != -1 || url_dfp.search("bondhushava/gallery") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Bondhushava_Articles_728x90_T1' -"+"-><div id='div-gpt-ad-5720320-2'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-5720320-2'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// bondhushava Sub-category
else if (url_dfp.search("/bs-") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Bondhushava_728x90_T1' -"+"-><div id='div-gpt-ad-5720320-1'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-5720320-1'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// bondhushava Landing
else if (url_dfp.search("/bondhushava") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Bondhushava_728x90_T1' -"+"-><div id='div-gpt-ad-5720320-1'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-5720320-1'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}



// kishoralo Details Article / Gallery
else if (url_dfp.search("kishoralo/article/") != -1 || url_dfp.search("kishoralo/gallery/") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Kishoralo_Articles_728x90_T1' -"+"-><div id='div-gpt-ad-5720320-13'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-5720320-13'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// kishoralo Archive / Listing
else if (url_dfp.search("kishoralo/article") != -1 || url_dfp.search("kishoralo/gallery") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Kishoralo_Articles_728x90_T1' -"+"-><div id='div-gpt-ad-5720320-13'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-5720320-13'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// kishoralo Sub-category
else if (url_dfp.search("/kia-") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Kishoralo_728x90_T1' -"+"-><div id='div-gpt-ad-5720320-12'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-5720320-12'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
/* kishoralo Landing */
else if (url_dfp.search("/kishoralo") != -1) { 
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Kishoralo_728x90_T1' -"+"-><div id='div-gpt-ad-5720320-12'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-5720320-12'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}

// Life Style Details Article / Gallery / Archive Listing
else if (url_dfp.search("life-style/article") != -1 || url_dfp.search("life-style/gallery") != -1
|| url_dfp.search("we-are/article") != -1 || url_dfp.search("we-are/gallery") != -1
|| url_dfp.search("art-and-literature/article") != -1 || url_dfp.search("art-and-literature/gallery") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Lifestyle_Articles_728x90_T1' -"+"-><div id='div-gpt-ad-23351-3'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-23351-3'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// Life Style Sub-category
else if (url_dfp.search("/lifestyle-") != -1 || url_dfp.search("/we-are-") != -1 || url_dfp.search("/female-stage") != -1 || url_dfp.search("/personality") != -1 || url_dfp.search("/torun") != -1 || url_dfp.search("/international-womens-day") != -1 || url_dfp.search("/art-and-literature-") != -1 || url_dfp.search("/poem") != -1 || url_dfp.search("/short-stories") != -1 || url_dfp.search("/industrial-art") != -1 || url_dfp.search("/meeting") != -1 || url_dfp.search("/treatise") != -1 || url_dfp.search("/translation") != -1 || url_dfp.search("/children-s-literature") != -1 || url_dfp.search("/book-discussion") != -1 || url_dfp.search("/child") != -1 || url_dfp.search("/kishor") != -1 || url_dfp.search("/personality") != -1 || url_dfp.search("/torun") != -1 || url_dfp.search("/probashi") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Lifestyle_Sub_728x90_T1' -"+"-><div id='div-gpt-ad-23351-2'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-23351-2'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// Life Style Landing
else if (url_dfp.search("/life-style") != -1 || url_dfp.search("/we-are") != -1 || url_dfp.search("/art-and-literature") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Lifestyle_728x90_T1' -"+"-><div id='div-gpt-ad-23351-1'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-23351-1'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// Entertainment Details Article / Gallery
else if (url_dfp.search("entertainment/article/") != -1 || url_dfp.search("entertainment/gallery/") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Ent_Articles_728x90_T1' -"+"-><div id='div-gpt-ad-31848-3'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-31848-3'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// Entertainment Archive / Listing
else if (url_dfp.search("entertainment/article") != -1 || url_dfp.search("entertainment/gallery") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Ent_Articles_728x90_T1' -"+"-><div id='div-gpt-ad-31848-3'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-31848-3'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// Entertainment Sub Category
else if(url_dfp.search("/entertainment-") != -1 || url_dfp.search("/alapon") != -1 || url_dfp.search("/music") != -1 || url_dfp.search("/dance") != -1 || url_dfp.search("/somalochona") != -1 || url_dfp.search("/tarokader-lekha") != -1){
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Ent_Sub_728x90_T1' -"+"-><div id='div-gpt-ad-31848-2'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-31848-2'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// Entertainment Landing
else if (url_dfp.search("/entertainment") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Entertainment_728x90_T1' -"+"-><div id='div-gpt-ad-31848-1'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-31848-1'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// Business Details Article / Gallery
else if (url_dfp.search("economy/article/") != -1 || url_dfp.search("economy/gallery/") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Business_Articles_728x90_T1' -"+"-><div id='div-gpt-ad-85668-3'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-85668-3'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// Business Archive / Listing
else if (url_dfp.search("economy/article") != -1 || url_dfp.search("economy/gallery") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Business_Articles_728x90_T1' -"+"-><div id='div-gpt-ad-85668-3'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-85668-3'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// Business Sub-category
else if (url_dfp.search("/economy-") != -1 || url_dfp.search("/budget") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Business_Sub_728x90_T1' -"+"-><div id='div-gpt-ad-85668-2'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-85668-2'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// Business Landing
else if (url_dfp.search("/economy") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Business_728x90_T1' -"+"-><div id='div-gpt-ad-85668-1'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-85668-1'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}






// northamerica Details Article / Gallery
else if (url_dfp.search("northamerica/article/") != -1 || url_dfp.search("northamerica/gallery/") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Northamerica_Articles_728x90_T1' -"+"-><div id='div-gpt-ad-4549433-3'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-4549433-3'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}

// northamerica Archive / Listing
else if (url_dfp.search("northamerica/article") != -1 || url_dfp.search("northamerica/gallery") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Northamerica_Articles_728x90_T1' -"+"-><div id='div-gpt-ad-4549433-3'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-4549433-3'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// northamerica Sub-category
else if (url_dfp.search("/northamerica-") != -1 || url_dfp.search("/canada") != -1  || url_dfp.search("/america") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Northamerica_Sub_728x90_T1' -"+"-><div id='div-gpt-ad-4549433-2'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-4549433-2'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// northamerica Landing
else if (url_dfp.search("/northamerica") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Northamerica_728x90_T1' -"+"-><div id='div-gpt-ad-4549433-1'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-4549433-1'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}




// Education Details Article / Gallery
else if (url_dfp.search("education/article/") != -1 || url_dfp.search("education/gallery/") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Edu_Articles_728x90_T1' -"+"-><div id='div-gpt-ad-81614-3'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-81614-3'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// Education Archive / Listing
else if (url_dfp.search("education/article") != -1 || url_dfp.search("education/gallery") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Edu_Articles_728x90_T1' -"+"-><div id='div-gpt-ad-81614-3'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-81614-3'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// Education Sub-category
else if (url_dfp.search("/education-") != -1 || url_dfp.search("/institution") != -1 || url_dfp.search("/meritorious") != -1 || url_dfp.search("/preparation") != -1 || url_dfp.search("/jenerakhun") != -1 || (url_dfp.search("-education") != -1 && url_dfp.search("opinion-education") == -1)) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Edu_Sub_728x90_T1' -"+"-><div id='div-gpt-ad-81614-2'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-81614-2'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// Education Landing
else if (url_dfp.search("/education") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Education_728x90_T1' -"+"-><div id='div-gpt-ad-81614-1'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-81614-1'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// Protichinta Site
else if (url_dfp.search("/protichinta") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Protichinta_Home_728x90_T1' -"+"-><div id='div-gpt-ad-4549433-4'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-4549433-4'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// Naksha Landing
else if (url_dfp.search("/naksha") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Naksha_728x90_T1' -"+"-><div id='div-gpt-ad-16530-2'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-16530-2'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// shapno Landing
else if (url_dfp.search("/shapno") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Shapno_728x90_T1' -"+"-><div id='div-gpt-ad-16530-3'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-16530-3'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// adhuna Landing
else if (url_dfp.search("/adhuna") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Adhuna_728x90_T1' -"+"-><div id='div-gpt-ad-16530-4'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-16530-4'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// holiday Landing
else if (url_dfp.search("/holiday") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Holiday_728x90_T1' -"+"-><div id='div-gpt-ad-16530-5'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-16530-5'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// roshalo details article / archive listing
else if (url_dfp.search("roshalo/article") != -1 || url_dfp.search("roshalo/gallery") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Roshalo_Articles_728x90_T1' -"+"-><div id='div-gpt-ad-1837451-1'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-1837451-1'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// roshalo Landing
else if (url_dfp.search("/roshalo") != -1 && url_dfp.search("/roshalo/") == -1 ) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Roshalo_728x90_T1' -"+"-><div id='div-gpt-ad-16530-6'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-16530-6'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// ananda Landing
else if (url_dfp.search("/ananda") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Ananda_728x90_T1' -"+"-><div id='div-gpt-ad-16530-7'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-16530-7'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// All Features Landing
else if (url_dfp.search("/features") != -1 || url_dfp.search("/sabar-age-shisu") != -1 || url_dfp.search("/gollachut") != -1 ||
url_dfp.search("/anna-alo") != -1 || url_dfp.search("/shilpo-o-sahitto") != -1 || url_dfp.search("/alokito-chittagong") != -1 ||
url_dfp.search("/amader-kotha-shono") != -1 || url_dfp.search("/bondhushava") != -1 || url_dfp.search("/projonmo-dot-com") != -1 || url_dfp.search("/choltibishow") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Features_728x90_T1' -"+"-><div id='div-gpt-ad-16530-1'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-16530-1'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// Photo View
else if (url_dfp.search("photo/gallery/") != -1 || url_dfp.search("cartoon/gallery/") != -1 ) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'photos_views_728x90_T1' -"+"-><div id='div-gpt-ad-79289-2'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-79289-2'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// Photo Landing
else if (url_dfp.search("/photo") != -1 || url_dfp.search("/cartoon") != -1  ) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Photos_728x90_T1' -"+"-><div id='div-gpt-ad-79289-1'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-79289-1'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// Video Watch
else if (url_dfp.search("video/watch/") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'VideosViews_728x90_T1' -"+"-><div id='div-gpt-ad-79289-4'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-79289-4'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// Video Landing
else if (url_dfp.search("/video") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'Videos_728x90_T1' -"+"-><div id='div-gpt-ad-79289-3'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-79289-3'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// All Other News Archive Listing
else if (url_dfp.search("/article") != -1 || url_dfp.search("/gallery") != -1 || url_dfp.search("/specialsupplement-") != -1 || url_dfp.search("/topic/") != -1 || url_dfp.search("/advertise") != -1) {
		document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'News_Articles_728x90_T1' -"+"-><div id='div-gpt-ad-10691-3'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-10691-3'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// All Other News Sub Section
else if (url_dfp.search("/bangladesh-") != -1 || url_dfp.search("/international-") != -1 || url_dfp.search("/opinion-") != -1 || url_dfp.search("/durporobash-") != -1  || url_dfp.search("/pachmisheli") != -1   || url_dfp.search("/northamerica-") != -1 || url_dfp.search("/america") != -1 || url_dfp.search("/canada") != -1 || url_dfp.search("/election") != -1) {
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'News_Sub_728x90_T1' -"+"-><div id='div-gpt-ad-10691-2'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-10691-2'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}
// All Other News Landing
else{
	document.write("<div class='common_google_ads_top'><!-- Async AdSlot for Ad unit 'News_728x90_T1' -"+"-><div id='div-gpt-ad-10691-1'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-10691-1'); });" + "</"+"scr"+"ipt>"+"</div></div>");
}

$(document).ready(function(e) {

if($('.subpage_logo').length > 0){
$('.secondary_header').addClass('has_sub');
}
});
</script>
<script>
  googletag.cmd.push(function() {
if (url_dfp.search("/bangladesh") != -1 || url_dfp.search("/international") != -1 || url_dfp.search("/opinion") != -1 || url_dfp.search("/durporobash") != -1  || url_dfp.search("/pachmisheli") != -1  || url_dfp.search("/election") != -1 || url_dfp.search("/topic") != -1 || url_dfp.search("/photo") != -1 || url_dfp.search("/specialsupplement") != -1|| url_dfp.search("/cartoon") != -1 || url_dfp.search("/video") != -1 ) {
	googletag.defineOutOfPageSlot('/85406138/News_Int_660x440', 'div-gpt-ad-1499318314988-6').addService(googletag.pubads());  
}
else if(url_dfp.search("/sports-fixture") != -1){

}
else if (url_dfp.search("/sports") != -1 ) {
	googletag.defineOutOfPageSlot('/85406138/Sports_Int_660x440', 'div-gpt-ad-1499318314988-8').addService(googletag.pubads());
}
else if (url_dfp.search("/fifa-world-cup") != -1 ) {
	googletag.defineOutOfPageSlot('/85406138/Sports_Int_660x440', 'div-gpt-ad-1499318314988-8').addService(googletag.pubads());
}
else if(url_dfp.search("/entertainment") != -1 || url_dfp.search("/alapon") != -1 || url_dfp.search("/music") != -1 || url_dfp.search("/dance") != -1 || url_dfp.search("/somalochona") != -1 || url_dfp.search("/tarokader-lekha") != -1){
	googletag.defineOutOfPageSlot('/85406138/Entertainment_Int_660x440', 'div-gpt-ad-1499318314988-2').addService(googletag.pubads());
}
else if (url_dfp.search("/lifestyle") != -1 || url_dfp.search("/we-are-") != -1 || url_dfp.search("/female-stage") != -1 || url_dfp.search("/personality") != -1 || url_dfp.search("/torun") != -1 || url_dfp.search("/international-womens-day") != -1 || url_dfp.search("/art-and-literature-") != -1 || url_dfp.search("/poem") != -1 || url_dfp.search("/short-stories") != -1 || url_dfp.search("/industrial-art") != -1 || url_dfp.search("/meeting") != -1 || url_dfp.search("/treatise") != -1 || url_dfp.search("/translation") != -1 || url_dfp.search("/children-s-literature") != -1 || url_dfp.search("/book-discussion") != -1 || url_dfp.search("/child") != -1 || url_dfp.search("/kishor") != -1 || url_dfp.search("/personality") != -1 || url_dfp.search("/torun") != -1 || url_dfp.search("/probashi") != -1) {
	googletag.defineOutOfPageSlot('/85406138/Lifestyle_Int_660x440', 'div-gpt-ad-1499318314988-4').addService(googletag.pubads());
}
else if (url_dfp.search("/technology") != -1) {	
	googletag.defineOutOfPageSlot('/85406138/Tech_Int_660x440', 'div-gpt-ad-1499318314988-9').addService(googletag.pubads());
}

else if (url_dfp.search("/economy") != -1 || url_dfp.search("/budget") != -1) {
	googletag.defineOutOfPageSlot('/85406138/Economy_Int_660x440', 'div-gpt-ad-1499318314988-0').addService(googletag.pubads());
}

else if (url_dfp.search("/northamerica") != -1 || url_dfp.search("/canada") != -1  || url_dfp.search("/america") != -1) {
	googletag.defineOutOfPageSlot('/85406138/Northamerica_Int_660x440', 'div-gpt-ad-1499318314988-7').addService(googletag.pubads());
}

else if (url_dfp.search("/education") != -1 || url_dfp.search("/institution") != -1 || url_dfp.search("/meritorious") != -1 || url_dfp.search("/preparation") != -1 || url_dfp.search("/jenerakhun") != -1 || (url_dfp.search("-education") != -1 && url_dfp.search("opinion-education") == -1)) {
	googletag.defineOutOfPageSlot('/85406138/Education_Int_660x440', 'div-gpt-ad-1499318314988-1').addService(googletag.pubads());
}
else if (url_dfp.search("/naksha") != -1 || url_dfp.search("/shapno") != -1 || url_dfp.search("/adhuna") != -1 || url_dfp.search("/holiday") != -1 || url_dfp.search("roshalo") != -1 ||url_dfp.search("/ananda") != -1 ) {	
	googletag.defineOutOfPageSlot('/85406138/Naksha_Int_660x440', 'div-gpt-ad-1499318314988-5').addService(googletag.pubads());
}
else if (url_dfp.search("/features") != -1 || url_dfp.search("/sabar-age-shisu") != -1 || url_dfp.search("/gollachut") != -1 ||
url_dfp.search("/anna-alo") != -1 || url_dfp.search("/shilpo-o-sahitto") != -1 || url_dfp.search("/alokito-chittagong") != -1 ||
url_dfp.search("/amader-kotha-shono") != -1 || url_dfp.search("/projonmo-dot-com") != -1 || url_dfp.search("/choltibishow") != -1) {
		googletag.defineOutOfPageSlot('/85406138/Features_Int_660x440', 'div-gpt-ad-1499318314988-3').addService(googletag.pubads());
}else if(url_dfp.search("/sruti") != -1){

}

    googletag.pubads().enableSingleRequest();
    googletag.pubads().collapseEmptyDivs();
    googletag.enableServices();
  });
</script></div>
<div class="container pb16">
<div class="breadcrumb ">
<ul><li itemscope itemtype="http://data-vocabulary.org/Breadcrumb"><a itemprop=url href="http://www.prothomalo.com/"><strong itemprop=title>প্রচ্ছদ</strong></a></li><li itemscope itemtype="http://data-vocabulary.org/Breadcrumb"><a itemprop=url href="http://www.prothomalo.com/bangladesh"><strong itemprop=title>বাংলাদেশ</strong></a></li></ul>
</div>
</div>
</div>
</div>
<div class=pagemaker><div id=div_1627 class="p     _col"><div class=inner><div id=wrapper_56918 class="wrapper   container_white_bg "><div class=inner><div id=div_56919 class="p_p     _col"><div class=inner><div id=widget_56920 class="widget_color_ widget_wrap"><div class="detail_widget_banner  widget">	<div class=content_detail>
</div>
</div></div></div></div></div></div><div id=wrapper_1635 class="wrapper special_32_5_67_5  container_white_bg container_bottom_padding "><div class=inner><div id=div_1636 class="p_d   container_fixed_height  _col"><div class=inner><div id=widget_51897 class="widget_color_ widget_wrap"><div class="detail_widget  widget">	<div class="content_detail detail">
<div class=row>
<div class=left_category>
<div class=col_in>
<a class=category_name href="/bangladesh">বাংলাদেশ সংবাদ</a>
</div>
</div>
<div class=right_title>
<h1 class="title mb10">সুবর্ণচরে ধর্ষণের ঘটনার সঙ্গে ভোটের সম্পর্ক পায়নি মানবাধিকার কমিশন</h1>
</div>
</div>
<div class="spacer mb24"></div>
<div class="row detail_holder">
<div class=left_part>
<div class=col_in>
<div class=additional_info_container>
<div class="author each_row"><span class=name>মানসুরা হোসাইন, ঢাকা</span></div>
<div class="time each_row">
<span itemprop=datePublished content="2019-01-13T13:54:00+06:00">১৩ জানুয়ারি ২০১৯, ১৩:৫৪</span>
<br>
আপডেট:
<span itemprop=dateModified content="2019-01-13T15:18:17+06:00">১৩ জানুয়ারি ২০১৯, ১৫:১৮</span></div>
<div class="each_row do_not_print">
<div class="social_shares roundicons" data-show="print,facebook,twitter,googlePlus,viber,whatsapp" data-hide=""></div>
</div>
<div class="comment_and_like each_row dn do_not_print">
</div>
<div class="each_row do_not_print">
<div class=fb-save data-uri="" data-size=large></div>
</div>
</div>
</div>
</div>
<div class=right_part>
<div class=col_in>
<article itemscope itemtype="http://schema.org/Article" class="jw_detail_content_holder content mb16">
<div itemprop=articleBody class=viewport>
<noscript id=ari-noscript><p><img class="jwMediaContent image alignleft" itemprop=image data-jadewitsmedia="{'id':'1199871','name':'ধর্ষণ','caption':'','path':'media/2018/03/18/cc1107dbb1c246a9093a95ef8df7e78e-5aae1122a6fb1.jpg','ext':'jpg','type':'image','thumb':'//paloimages.prothom-alo.com/contents/cache/images/110x110x1/uploads/media/2018/03/18/cc1107dbb1c246a9093a95ef8df7e78e-5aae1122a6fb1.jpg','pushClass':'jwMediaContent','width':'250','height':139,'title':'','alt':'','align':'alignleft','link':'','target':''}" width=250 src="https://paloimages.prothom-alo.com/contents/cache/images/250x0x1/uploads/media/2018/03/18/cc1107dbb1c246a9093a95ef8df7e78e-5aae1122a6fb1.jpg"/>জাতীয় মানবাধিকার কমিশনের তথ্যানুসন্ধান প্রতিবেদন বলছে, সুবর্ণচরে ধর্ষণের শিকার নারীকে গুরুতর আঘাত করা এবং তাঁকে ধর্ষণ করার অভিযোগের প্রাথমিক সত্যতা পাওয়া গেছে। তবে একাদশ জাতীয় সংসদ নির্বাচনের সঙ্গে এই মারধর ও ধর্ষণের শিকার হওয়ার কোনো সম্পর্ক তদন্তকালে তদন্ত কমিটি খুঁজে পায়নি। বরং ওই নারীর স্বামীর দায়ের করা এজাহারের ভাষ্য মতে, পূর্ব শত্রুতার জেরেই এ ঘটনা ঘটেছে।<br/><br/>এ বিষয়ে জাতীয় মানবাধিকার কমিশনের চেয়ারম্যান কাজী রিয়াজুল হক প্রথম আলোকে বলেন, কমিশনের তদন্ত কমিটি ধর্ষণ ও গুরুতর আঘাতের সঙ্গে একাদশ জাতীয় সংসদ নির্বাচনের কোনো সম্পর্ক আছে বলে প্রমাণ পায়নি। তবে প্রাথমিকভাবে ওই নারী যে ধর্ষণের শিকার হয়েছেন, তার সত্যতা মিলেছে। এ ক্ষেত্রে মানবাধিকার লঙ্ঘনের ঘটনা ঘটেছে। কমিশনের পক্ষ থেকে যথাযথ তদন্ত করে আসামিদের দৃষ্টান্তমূলক শাস্তির আওতায় আনার সুপারিশ করা হয়েছে, ঘটনার সঙ্গে যে বা যারাই জড়িত থাকুক না কেন।</p>
<p>তবে ধর্ষণের শিকার ওই নারী ঘটনার পর থেকে এখন পর্যন্ত বলে আসছেন, ভোটের দিন ধানের শীষে ভোট দেওয়াকে কেন্দ্র করেই তাঁকে দেখে নেওয়ার হুমকি দিয়েছিলেন আসামিরা। ভোটের দিন রাতেই ধর্ষণের ঘটনা ঘটে।</p>
<p>প্রথম আলোর সংগৃহীত ভিডিওতে শোনা যায়, ধর্ষণের শিকার ওই নারী গণমাধ্যমকর্মীদের বলছেন যে তাঁকে নৌকায় ভোট দিতে বলা হলে তিনি জানান ধানের শীষে ভোট দেবেন। তিনি ধানের শীষেই ভোট দেন। তখন একজন বলে, তোর কপালে শনি আছে। তারপর রাতেই ১০ জন মিলে তাঁকে মারধর ও ধর্ষণ করেন।</p>
<p>গতকাল শনিবার রাতে টেলিফোনে ধর্ষণের শিকার ওই নারী প্রথম আলোকে বলেন, আগে থেকে শত্রুতা থাকলে আসামিরা তো আগেই ক্ষতি করত। তিনি কোনো দল করেন না দাবি করে বলেন, ভোটকেন্দ্রে গিয়ে তিনি নিজের ইচ্ছেমতো ধানের শীষে ভোট দেন। তবে ভোটের কাগজ কেমনে করে ভাঁজ করতে হবে বা কোথায় রাখতে হবে, তা জানা না থাকায় সেখানে উপস্থিত মামলার আসামিদের হাতেই তিনি তা দেন। তখন একজন ধমক দিয়ে বলে, সন্ধ্যাকালে খবর আছে।</p>
<p>তবে মানবাধিকার কমিশনের তদন্ত প্রতিবেদনে উল্লেখ করা হয়েছে, &lsquo;মামলার এজাহারে ওই নারীর ধানের শীষের নেতা-কর্মী-সমর্থক হওয়া, তাঁর ধানের শীষে ভোট দেওয়া, আসামিরা নৌকা প্রতীকের নেতা-কর্মী-সমর্থক ও পোলিং এজেন্ট হওয়া, <a href="https://election.prothomalo.com" target=_blank>একাদশ জাতীয় সংসদ নির্বাচনকে</a> কেন্দ্র করে নির্বাচনী বিরোধের জের ধরে মারধর বা ধর্ষণের শিকার হওয়া, তা উল্লেখ নেই। বরং এজাহারে সুস্পষ্টভাবে বলা হয়েছে যে আসামিরা পূর্ব শত্রুতার জের ধরে মারধর ও ধর্ষণ করে। এ ছাড়া ওই নারী তদন্ত কমিটির সামনে দেওয়া জবানবন্দির কোথাও বলেননি যে তিনি ধানের শীষে ভোট দিয়েছেন। তাঁর স্বামীও এসব কথা বলেননি।&rsquo; স্বামী-স্ত্রীর জবানবন্দি থেকেই প্রতিবেদনের উপসংহার হিসেবে বলা হয়েছে, &lsquo;একাদশ সংসদ নির্বাচনে ধানের শীষে ভোট দেওয়া বা ভোট দেওয়ার কারণে এ ঘটনা ঘটেছে বা আসামিরা আওয়ামী লীগের কর্মী হওয়া বা আওয়ামী লীগের কোনো কর্মীর মাধ্যমে ওই নারীকে মারপিট ও ধর্ষণের শিকার হওয়ার প্রমাণ পাওয়া যায় না।&rsquo;<br/> <br/>ঘটনার পর আইন ও সালিশ কেন্দ্র (আসক) একটি প্রতিনিধি দল পাঠায় সুবর্ণচরে। এ দল ফিরে এসে লিখিত প্রতিবেদন দেয়নি। তবে আসকের নির্বাহী পরিচালক শীপা হাফিজা প্রথম আলোকে বলেন, &lsquo;আমাদের প্রতিনিধি দলকে ধর্ষণের শিকার নারী পূর্বশত্রুতার জেরের কথা যেমন বলেছেন, তেমনি ভোটের দিনের ঘটনাও বলেছেন।&rsquo;</p>
<p>জাতীয় মানবাধিকার কমিশনের তথ্যানুসন্ধান প্রতিবেদনের কপি আইন, বিচার ও সংসদ বিষয়ক মন্ত্রণালয়ের সচিব, স্বরাষ্ট্র মন্ত্রণালয়ের জননিরাপত্তা বিভাগের সচিব বরাবর পাঠানো হয়েছে।</p>
<p>গত ১ জানুয়ারি মানবাধিকার কমিশনের পক্ষ থেকে কমিশনের সম্মেলনকক্ষে নির্বাচন সংক্রান্ত এক সংবাদ সম্মেলনে সুবর্ণচরের ঘটনার বিষয়ে কমিশনের দৃষ্টি আকর্ষণ করা হয়। কমিশনের চেয়ারম্যান কাজী রিয়াজুল হক তাৎক্ষণিকভাবে কমিশনের পরিচালক (অভিযোগ ও তদন্ত, জেলা ও দায়রা জজ) এর নেতৃত্বে তিন সদস্য বিশিষ্ট তথ্যানুসন্ধান কমিটি গঠন করেন। এই দল পরের দিনই ঘটনাস্থলে গিয়ে ওই নারী, নারীর স্বামী, থানার ভারপ্রাপ্ত কর্মকর্তা, নোয়াখালী জেনারেল হাসপাতালের আবাসিক চিকিৎসক, পুলিশ সুপার, জেলা প্রশাসকসহ সংশ্লিষ্টদের সঙ্গে কথা বলেন। এরপর কমিটি কমিশনের চেয়ারম্যানকে প্রতিবেদনটি জমা দেয়। <a href="http://nhrc.portal.gov.bd/sites/default/files/files/nhrc.portal.gov.bd/page/22efa146_59ac_45b2_87d4_c547014869ea/%E0%A6%AA%E0%A7%8D%E0%A6%B0%E0%A6%A4%E0%A6%BF%E0%A6%AC%E0%A7%87%E0%A6%A6%E0%A6%A8.pdf" rel=nofollow target=_blank>এই প্রতিবেদনের কপি কমিশনের ওয়েবসাইটে</a> আছে।</p>
<p>কমিশনের প্রতিবেদনে হাসপাতালের আবাসিক চিকিৎসক সৈয়দ মহিউদ্দিন আবদুল আজিমের জবানবন্দি, ইনজুরি সার্টিফিকেট, এক্স-রে প্রতিবেদন, থানার ভারপ্রাপ্ত কর্মকর্তাসহ সবার বক্তব্য উল্লেখ করা হয়েছে। সব বক্তব্য বিশ্লেষণ করে কমিশনের তদন্ত কমিটি যে মতামত দিয়েছে তা হলো, ওই নারীকে গুরুতর জখম করা হয়েছে এবং ধর্ষণ করা হয়েছে।</p>
<p>(প্রতিবেদন তৈরিতে সহায়তা করেছেন প্রথম আলোর নোয়াখালীর নিজস্ব প্রতিবেদক মাহবুবুর রহমান)</p>
<p>আরও পড়ুন:&nbsp;<br/><a href="https://www.prothomalo.com/bangladesh/article/1574305/" target=_blank>গ্রেপ্তার ১২, সাতজনের স্বীকারোক্তিমূলক জবানবন্দি<br/></a><a href="https://www.prothomalo.com/bangladesh/article/1573899/" target=_blank>প্রধান আসামিসহ আরও দুজনের স্বীকারোক্তি<br/></a><a href="https://www.prothomalo.com/bangladesh/article/1574151/" target=_blank>সুবর্ণচরে গণধর্ষণ &lsquo;দলীয় সুযোগের কারণেই&rsquo;: নিপীড়নবিরোধী শিক্ষার্থী জোট<br/></a><a href="https://www.prothomalo.com/opinion/article/1573844/" target=_blank>তবে এই ধর্ষকদের খুঁজে পাওয়া যাবে না?<br/></a><a href="https://www.prothomalo.com/opinion/article/1573017/" target=_blank>সুবর্ণচরের কালরাত<br/></a><a href="https://www.prothomalo.com/bangladesh/article/1573324/" target=_blank>&lsquo;সুবর্ণচরের ঘটনায় আ.লীগ গণশত্রুতে পরিণত হয়েছে&rsquo;<br/></a><a href="https://www.prothomalo.com/bangladesh/article/1573240/" target=_blank>&lsquo;শক্তির অপপ্রয়োগের প্রমাণ সুবর্ণচরের গণধর্ষণ&rsquo;<br/></a><a href="https://www.prothomalo.com/bangladesh/article/1573231/" target=_blank>আমরা ক্ষুব্ধ, উদ্বিগ্ন ও মর্মাহত: ড. কামাল</a></p>
<p>&nbsp;</p></noscript>
</div>
<script>
								//console.log(current_page_url);
								var $div = $('<div>').append($('#ari-noscript').text() ).attr('itemprop','articleBody' ).addClass('viewport');
								var $images = $div.find('.jwMediaContent');
								for(var i in $images) {
									if(typeof $images[i]=='object')$($images[i]).removeAttr('src' ).removeClass(function () {
										return $(this).attr('class').replace(/\b(?:alignright|alignleft)\b\s*/g, '');
									});;//.removeAttr('class')
								}
								$('#ari-noscript' ).parent().replaceWith($div);
								var parentWidth = $div.width();
								$images.each(function(){
									var data = $.parseJSON($(this).data('jadewitsmedia').replace(/'/g, '"'));
									//console.log($(this ).attr('class'));
									if(data){
										var prop = {
											width : 0,
											height:0,
											wrapCaption:jwARI.caption(data['title'],data['caption']),
											viewPort:'.jw_detail_content_holder',
											url:cannonical_url +'#image-'+data.id
										};
										if(data['align']==''){
											if($(this ).hasClass('alignright')) data['align'] = 'alignright';
											if($(this ).hasClass('alignleft')) data['align'] = 'alignleft';
										}
										if(data['align']=='alignright' || data['align']=='alignleft'){
											if(parseFloat(data.width) >Math.floor(parentWidth*0.62)){
												prop.width = parentWidth;
												if(data.height && data.height>64) {
													prop.height = jwARI.ratio(data.height,data.width,parentWidth);
												}
												else {
													delete prop.height;
													delete data.height;
												}
												data['align_current'] = 'alignfull';
											}else if(!data.width){
												prop.width = 300;
												delete prop.height;
												delete data.height;
											}else{
												prop.width = data.width;
												if(data.height && data.height>64){
													prop.height = data.height;
												}
												else {
													delete prop.height;
													delete data.height;
												}
											}
										}else{
											if(data.height && data.height<50) {
												delete prop.height;
												delete data.height;
											}else{
												if(data.width){
													prop.width = data.width;
													prop.height = data.height;
												}else{
													delete prop.width;
													delete data.width;
												}
												prop.height = data.height;
											}
											data['align'] = 'alignfull';
										}
										var tmp = $.extend(prop,data);
										$(this ).data('ari',tmp);
										jwARI.fetch($(this));
									}
								});
							</script>
</article>
<div class=more_and_tag>
<a class=more_link href="/bangladesh/article">আরও সংবাদ</a>
<div class=content_tags>
<h4 class=content_tags_header>বিষয়: </h4>
<div class=topic_list>
<a href="//www.prothomalo.com/topic/%E0%A6%A7%E0%A6%B0%E0%A7%8D%E0%A6%B7%E0%A6%A3"><strong>ধর্ষণ</strong></a>
<a href="//www.prothomalo.com/topic/%E0%A6%AE%E0%A6%BE%E0%A6%A8%E0%A6%AC%E0%A6%BE%E0%A6%A7%E0%A6%BF%E0%A6%95%E0%A6%BE%E0%A6%B0"><strong>মানবাধিকার</strong></a>
<a href="//www.prothomalo.com/topic/%E0%A6%8F%E0%A6%95%E0%A6%BE%E0%A6%A6%E0%A6%B6-%E0%A6%B8%E0%A6%82%E0%A6%B8%E0%A6%A6-%E0%A6%A8%E0%A6%BF%E0%A6%B0%E0%A7%8D%E0%A6%AC%E0%A6%BE%E0%A6%9A%E0%A6%A8"><strong>একাদশ সংসদ নির্বাচন</strong></a>
<a href="//www.prothomalo.com/topic/%E0%A6%85%E0%A6%AA%E0%A6%B0%E0%A6%BE%E0%A6%A7"><strong>অপরাধ</strong></a>
<a href="//www.prothomalo.com/topic/%E0%A6%A8%E0%A7%8B%E0%A7%9F%E0%A6%BE%E0%A6%96%E0%A6%BE%E0%A6%B2%E0%A7%80"><strong>নোয়াখালী</strong></a>
</div>
</div>
</div>
<div class=additional_bottom_container>
<div class="social_shares roundicons" data-show="facebook,twitter,googlePlus,viber,whatsapp" data-hide="print,pinterest,instagram"></div>
<div class=fb-save data-uri="" data-size=large></div>
</div>
<script>
							
														
							
						</script>
</div>
</div>
</div>
<script>
				//$('.detail_holder .content blockquote').css({top:($('.detail_holder .left_part .col_in').outerHeight()+64)+'px'});
			</script>
</div>
<script>
				$('.jw_detail_content_holder iframe').each(jw_content_iframe_fix);
				jwFullScreen.init({
					hook:'.right_part',
					pop:'.pop-media-holder',
					cache:'800x0x0'
				});
				$('.social_shares' ).trigger('jadewitsShare');
			</script>
</div></div><div id=widget_99452 class="widget_color_ widget_wrap"><div class="widget_text  widget">	<div class="widget_text_inner aunqur">
<div class=content><script>
$(document).ready(function(){
	
	if($(".topic_list").is(':contains("নিরাপদ সড়ক দিবস")')){
		$(".common_google_ads_top").css('display','none');
		
		$(".header_ad_block.advertisement").append('<a href="http://bit.ly/nationalroadsafetyday2018" target="_blank"><img src="https://service.prothomalo.com/palo/road_safety/desk.gif" alt="Partex Gypsum" class="desktop_show"><img src="https://service.prothomalo.com/palo/road_safety/mob.gif" alt="Partex Gypsum" class="mobile_show"></a>');
		
		$('.r_1_ad').css('display','none');
		$(".Special_ad_r1").append('<a href="http://bit.ly/nationalroadsafetyday2018" target="_blank"><img src="https://service.prothomalo.com/palo/road_safety/r1.gif" alt="Partex Gypsum"></a>');
	}
});
</script></div>
</div>
</div></div></div></div><div id=div_1637 class="p_c  special_add   _col"><div class=inner><div id=widget_28306 class="widget_color_ widget_wrap"><div class="widget_text  widget">	<div class="widget_text_inner aunqur">
<div class=content><div class="common_google_ads r_1_ad">
<div id=div-gpt-ad-10691-11>
<script>
    googletag.cmd.push(function() { googletag.display('div-gpt-ad-10691-11'); });
  </script>
</div>
</div>
<div class=Special_ad_r1></div></div>
</div>
</div></div><div id=widget_56923 class="widget_color_ widget_wrap"><div class="contents_listing  widget">	<div class="contents  
			 
						 
			">
<div class=row><div class="col col1"><div class=col_in><div class=listing>	<div class="each col_in 
			has_image 
			image_left 
			content_capability_blog 
			content_type_article 
			responsive_image_hide_			 
			 
			m_show_featured_image_as_left 
						 
		">
<a class=link_overlay href="/bangladesh/article/1574384/%E2%80%98%E0%A6%AD%E0%A7%81%E0%A6%B2%E2%80%99-%E0%A6%B8%E0%A7%8D%E0%A6%AC%E0%A7%80%E0%A6%95%E0%A6%BE%E0%A6%B0-%E0%A6%95%E0%A6%B0%E0%A6%BE%E0%A7%9F-%E0%A6%A1.-%E0%A6%95%E0%A6%BE%E0%A6%AE%E0%A6%BE%E0%A6%B2%E0%A6%95%E0%A7%87-%E0%A6%A7%E0%A6%A8%E0%A7%8D%E0%A6%AF%E0%A6%AC%E0%A6%BE%E0%A6%A6-%E0%A6%A4%E0%A6%A5%E0%A7%8D%E0%A6%AF%E0%A6%AE%E0%A6%A8%E0%A7%8D%E0%A6%A4%E0%A7%8D%E0%A6%B0%E0%A7%80%E0%A6%B0"></a>
<div class=image>
<noscript id=ari-image-569231574384 data-ari="{&quot;path&quot;:&quot;media\/2019\/01\/13\/7839d0dd268e453ab4596db0f3f5da88-5c3ae9170e37b.jpg?jadewits_media_id=1409275&quot;,&quot;ratio&quot;:[16,9],&quot;alt&quot;:&quot;\u2018\u09ad\u09c1\u09b2\u2019 \u09b8\u09cd\u09ac\u09c0\u0995\u09be\u09b0 \u0995\u09b0\u09be\u09df \u09a1. \u0995\u09be\u09ae\u09be\u09b2\u0995\u09c7 \u09a7\u09a8\u09cd\u09af\u09ac\u09be\u09a6 \u09a4\u09a5\u09cd\u09af\u09ae\u09a8\u09cd\u09a4\u09cd\u09b0\u09c0\u09b0&quot;}">
<img src="//paloimages.prothom-alo.com/contents/cache/images/400x225x1/uploads/media/2019/01/13/7839d0dd268e453ab4596db0f3f5da88-5c3ae9170e37b.jpg?jadewits_media_id=1409275" alt="‘ভুল’ স্বীকার করায় ড. কামালকে ধন্যবাদ তথ্যমন্ত্রীর"/>
</noscript>
<script data-id=ari-image-569231574384>
								jwARI.fetch( $( '#ari-image-569231574384' ) );
							</script>
<span class=content_type></span>
</div>
<div class="info ">
<h2 class=title_holder>
<span class=title>‘ভুল’ স্বীকার করায় ড. কামালকে ধন্যবাদ তথ্যমন্ত্রীর</span>
</h2>
<div class=additional>
</div>
</div>
</div>
<div class="each col_in 
			has_image 
			image_left 
			content_capability_blog 
			content_type_article 
			responsive_image_hide_			 
			 
			m_show_featured_image_as_left 
						 
		">
<a class=link_overlay href="/bangladesh/article/1574357/%E0%A6%86%E0%A6%B8%E0%A6%BE%E0%A6%AE%E0%A6%BF-%E0%A6%A7%E0%A6%B0%E0%A6%BE-%E0%A6%A8%E0%A6%BF%E0%A7%9F%E0%A7%87-%E0%A6%B9%E0%A7%81%E0%A6%B2%E0%A7%81%E0%A6%B8%E0%A7%8D%E0%A6%A5%E0%A7%81%E0%A6%B2-%E0%A6%A8%E0%A6%BF%E0%A6%B9%E0%A6%A4-%E0%A7%A7-%E0%A6%86%E0%A6%B9%E0%A6%A4-%E0%A7%A7%E0%A7%AB"></a>
<div class=image>
<noscript id=ari-image-569231574357 data-ari="{&quot;path&quot;:&quot;media\/2017\/07\/26\/26c4860b3dce5043e9b75e8c73c0f567-59782ae36dabf.jpg?jadewits_media_id=930856&quot;,&quot;ratio&quot;:[16,9],&quot;alt&quot;:&quot;\u0986\u09b8\u09be\u09ae\u09bf \u09a7\u09b0\u09be \u09a8\u09bf\u09df\u09c7 \u09b9\u09c1\u09b2\u09c1\u09b8\u09cd\u09a5\u09c1\u09b2\u09c7 \u09a8\u09bf\u09b9\u09a4 \u09e7, \u0986\u09b9\u09a4 \u09e7\u09eb&quot;}">
<img src="//paloimages.prothom-alo.com/contents/cache/images/400x225x1/uploads/media/2017/07/26/26c4860b3dce5043e9b75e8c73c0f567-59782ae36dabf.jpg?jadewits_media_id=930856" alt="আসামি ধরা নিয়ে হুলুস্থুলে নিহত ১, আহত ১৫"/>
</noscript>
<script data-id=ari-image-569231574357>
								jwARI.fetch( $( '#ari-image-569231574357' ) );
							</script>
<span class=content_type></span>
</div>
<div class="info ">
<h2 class=title_holder>
<span class=title>আসামি ধরা নিয়ে হুলুস্থুলে নিহত ১, আহত ১৫</span>
</h2>
<div class=additional>
</div>
</div>
</div>
<div class="each col_in 
			has_image 
			image_left 
			content_capability_blog 
			content_type_article 
			responsive_image_hide_			 
			 
			m_show_featured_image_as_left 
						 
		">
<a class=link_overlay href="/bangladesh/article/1574353/%E0%A6%95%E0%A6%B2-%E0%A6%B2%E0%A6%BF%E0%A6%B8%E0%A7%8D%E0%A6%9F%E0%A7%87%E0%A6%B0-%E0%A6%B8%E0%A7%82%E0%A6%A4%E0%A7%8D%E0%A6%B0-%E0%A6%A7%E0%A6%B0%E0%A7%87-%E0%A6%AE%E0%A6%BF%E0%A6%B2%E0%A6%B2-%E0%A6%96%E0%A7%81%E0%A6%A8%E0%A6%BF%E0%A6%B0-%E0%A6%AA%E0%A6%B0%E0%A6%BF%E0%A6%9A%E0%A7%9F"></a>
<div class=image>
<noscript id=ari-image-569231574353 data-ari="{&quot;path&quot;:&quot;media\/2019\/01\/13\/bf5cb59ef6f7ea3739c800095c7d661e-5c3ad0e88eef5.jpg?jadewits_media_id=1409211&quot;,&quot;ratio&quot;:[16,9],&quot;alt&quot;:&quot;\u0995\u09b2 \u09b2\u09bf\u09b8\u09cd\u099f\u09c7\u09b0 \u09b8\u09c2\u09a4\u09cd\u09b0 \u09a7\u09b0\u09c7 \u09ae\u09bf\u09b2\u09b2 \u0996\u09c1\u09a8\u09bf\u09b0 \u09aa\u09b0\u09bf\u099a\u09df&quot;}">
<img src="//paloimages.prothom-alo.com/contents/cache/images/400x225x1/uploads/media/2019/01/13/bf5cb59ef6f7ea3739c800095c7d661e-5c3ad0e88eef5.jpg?jadewits_media_id=1409211" alt="কল লিস্টের সূত্র ধরে মিলল খুনির পরিচয়"/>
</noscript>
<script data-id=ari-image-569231574353>
								jwARI.fetch( $( '#ari-image-569231574353' ) );
							</script>
<span class=content_type></span>
</div>
<div class="info ">
<h2 class=title_holder>
<span class=title>কল লিস্টের সূত্র ধরে মিলল খুনির পরিচয়</span>
</h2>
<div class=additional>
</div>
</div>
</div>
<div class="each col_in 
			has_image 
			image_left 
			content_capability_blog 
			content_type_article 
			responsive_image_hide_			 
			 
			m_show_featured_image_as_left 
						 
		">
<a class=link_overlay href="/bangladesh/article/1574336/%E0%A6%AC%E0%A6%BE%E0%A6%AC%E0%A6%BE%E0%A6%95%E0%A7%87-%E0%A6%B6%E0%A6%BF%E0%A6%95%E0%A7%8D%E0%A6%B7%E0%A6%BE-%E0%A6%A6%E0%A6%BF%E0%A6%A4%E0%A7%87-%E0%A6%97%E0%A6%BF%E0%A7%9F%E0%A7%87-%E0%A6%96%E0%A7%81%E0%A6%A8"></a>
<div class=image>
<noscript id=ari-image-569231574336 data-ari="{&quot;path&quot;:&quot;media\/2018\/05\/17\/4fb23df05a789fa639db957342360b12-5afd1028a5bc5.jpg?jadewits_media_id=1262511&quot;,&quot;ratio&quot;:[16,9],&quot;alt&quot;:&quot;\u09ac\u09be\u09ac\u09be\u0995\u09c7 \u09b6\u09bf\u0995\u09cd\u09b7\u09be \u09a6\u09bf\u09a4\u09c7 \u0997\u09bf\u09df\u09c7 \u0996\u09c1\u09a8&quot;}">
<img src="//paloimages.prothom-alo.com/contents/cache/images/400x225x1/uploads/media/2018/05/17/4fb23df05a789fa639db957342360b12-5afd1028a5bc5.jpg?jadewits_media_id=1262511" alt="বাবাকে শিক্ষা দিতে গিয়ে খুন"/>
</noscript>
<script data-id=ari-image-569231574336>
								jwARI.fetch( $( '#ari-image-569231574336' ) );
							</script>
<span class=content_type></span>
</div>
<div class="info ">
<h2 class=title_holder>
<span class=title>বাবাকে শিক্ষা দিতে গিয়ে খুন</span>
</h2>
<div class=additional>
</div>
</div>
</div>
</div></div></div></div>	</div>
</div></div><div id=widget_28311 class="widget_color_ widget_wrap"><div class="widget_text  widget">	<div class="widget_text_inner aunqur">
<div class=content><div class=common_google_ads>
<div id=div-gpt-ad-10691-12>
<script>
    googletag.cmd.push(function() { googletag.display('div-gpt-ad-10691-12'); });
  </script>
</div>
</div>
<div class=Special_ad_r2></div></div>
</div>
</div></div><div id=widget_72996 class="widget_color_ widget_wrap"><div class="widget_text  widget">	<div class="widget_text_inner aunqur">
<div class=content><style>
.mi_24x24_zoomin {
    width: 32px;
    height: 32px;
    border-radius: 16px;
    float: left;
    background: url(//storage.googleapis.com/production-prothomalo/contents/uploads/media/2017/11/14/7b239bc050b256849d7c71e88ebaf242-5a0a9a1230546.png) no-repeat 0 0;
}

.mi_24x24_zoomout {
    width: 32px;
    height: 32px;
    border-radius: 16px;
    float: left;
    background: url(//storage.googleapis.com/production-prothomalo/contents/uploads/media/2017/11/14/08db1dcd9d7743855af0af47482b4547-5a0a9a122faec.png) no-repeat 0 0;
}
</style>
<script>
$(document).ready(function(e) {
	
	$('.comment_and_like.each_row.do_not_print').removeClass('dn');
    $('.left_part .comment_and_like').prepend('<a class="mr10 mi_24x24 mi_24x24_zoomout jw_content_zoom_out" title="Zoom Out" data-container="jw_detail_content_holder" href="javascript:">&nbsp;</a><a class="mr10 mi_24x24 mi_24x24_zoomin jw_content_zoom_in" title="Zoom In" data-container="jw_detail_content_holder" href="javascript:">&nbsp;</a>');
	
	
$('.jw_content_zoom_out').live('click',function(){
	el = $(".detail .content p");
	jw_change_font_size(el,-2);
	
	el = $(".content .jw_media_holder .jw_media_caption");
	jw_change_font_size(el,-2);
	
	});
	
$('.jw_content_zoom_in').live('click',function(){
	el = $(".detail .content p");
	jw_change_font_size(el,+2);
	
	el = $(".content .jw_media_holder .jw_media_caption");
	jw_change_font_size(el,+2);
	}); 
	
});
</script></div>
</div>
</div></div></div></div></div></div><div id=wrapper_74126 class="wrapper special_32_5_67_5  container_top_padding "><div class=inner><div id=div_74131 class="p_d     _col"><div class=inner><div id=widget_74141 class="widget_color_ widget_wrap"><div class="comments_widget  widget">	<div id=comments class=comment_div>
<div class=row>
<div class=left_part>
<div class=col_in>
<h4 class=comments_title>মন্তব্য </h4>
<div class=comment_account_wrap>
<span class=profile_link_holder></span>
</div>
</div>
</div>
<div class=right_part>
<div class=col_in>
<i id=login_prompt class=fake_ha></i>
<div id="" class="login_prompt dn">
<div class=login_register_link>
মন্তব্য করতে <a class=login href="https://profiles.prothomalo.com/login/?APP_ID=1&next=https%3A%2F%2Fwww.prothomalo.com%2Fbangladesh%2Farticle%2F1574390%2F%25E0%25A6%25B8%25E0%25A7%2581%25E0%25A6%25AC%25E0%25A6%25B0%25E0%25A7%258D%25E0%25A6%25A3%25E0%25A6%259A%25E0%25A6%25B0%25E0%25A7%2587-%25E0%25A6%25A7%25E0%25A6%25B0%25E0%25A7%258D%25E0%25A6%25B7%25E0%25A6%25A3%25E0%25A7%2587%25E0%25A6%25B0-%25E0%25A6%2598%25E0%25A6%259F%25E0%25A6%25A8%25E0%25A6%25BE%25E0%25A6%25B0-%25E0%25A6%25B8%25E0%25A6%2599%25E0%25A7%258D%25E0%25A6%2597%25E0%25A7%2587-%25E0%25A6%25AD%25E0%25A7%258B%25E0%25A6%259F%25E0%25A7%2587%25E0%25A6%25B0-%25E0%25A6%25B8%25E0%25A6%25AE%25E0%25A7%258D%25E0%25A6%25AA%25E0%25A6%25B0%25E0%25A7%258D%25E0%25A6%2595-%25E0%25A6%25AA%25E0%25A6%25BE%25E0%25A7%259F%25E0%25A6%25A8%25E0%25A6%25BF#comments">লগইন</a> করুন অথবা <a class=register href="https://profiles.prothomalo.com/register/?APP_ID=1&next=https%3A%2F%2Fwww.prothomalo.com%2Fbangladesh%2Farticle%2F1574390%2F%25E0%25A6%25B8%25E0%25A7%2581%25E0%25A6%25AC%25E0%25A6%25B0%25E0%25A7%258D%25E0%25A6%25A3%25E0%25A6%259A%25E0%25A6%25B0%25E0%25A7%2587-%25E0%25A6%25A7%25E0%25A6%25B0%25E0%25A7%258D%25E0%25A6%25B7%25E0%25A6%25A3%25E0%25A7%2587%25E0%25A6%25B0-%25E0%25A6%2598%25E0%25A6%259F%25E0%25A6%25A8%25E0%25A6%25BE%25E0%25A6%25B0-%25E0%25A6%25B8%25E0%25A6%2599%25E0%25A7%258D%25E0%25A6%2597%25E0%25A7%2587-%25E0%25A6%25AD%25E0%25A7%258B%25E0%25A6%259F%25E0%25A7%2587%25E0%25A6%25B0-%25E0%25A6%25B8%25E0%25A6%25AE%25E0%25A7%258D%25E0%25A6%25AA%25E0%25A6%25B0%25E0%25A7%258D%25E0%25A6%2595-%25E0%25A6%25AA%25E0%25A6%25BE%25E0%25A7%259F%25E0%25A6%25A8%25E0%25A6%25BF">নিবন্ধন</a> করুন
</div>
</div>
<div id=write_comments class="write_comments_form dn">
<form onSubmit="return false;" id=comment_form name=comment_form action="" method=post>
<input type=hidden name=fk_content_id value=1574390 />
<input type=hidden name=parent value=0 />
<input type=hidden name=label_depth value=0 />
<div class="textarea_holder comment_input input_wrap">
<textarea class="textarea jadewits_keyboard" name=comment cols=40 rows=4></textarea>
</div>
<div class=text_holder>আপনার পরিচয় গোপন রাখতে <label><input class=checkbox type=checkbox name=hidden_name id=hidden_name value=1> এখানে ক্লিক করুন।</label> <br> আমি <a target=_blank href="http://www.prothomalo.com/user-terms-and-conditions">নীতিমালা</a> মেনে মন্তব্য করছি।</div>
<div class=input_wrap><input type=button class="button_light comment_submit" name=jadewits_insert_update value="পাঠিয়ে দিন"></div>
<div class=comment_message></div>
</form>
</div>
<div class="discussion_toolbar_container dn">
<div class=discussion_toolbar_order>
<select id=jw_comments_order_by>
<option value=new>নতুন থেকে পুরোনো</option>
<option value=old>পুরোনো থেকে নতুন</option>
</select>
</div>
<div class="discussion_toolbar_show dn">
<span>Show</span>
<select>
<option value=25>25</option>
<option value=50>50</option>
<option value=100>100</option>
<option value=all>All</option>
</select>
</div>
<div class="discussion_toolbar_pagination dn">
<div class=discuss_pagination_list>
<a class=active href=javascript:>1</a>
<a href=javascript:>2</a>
<a href=javascript:>3</a>
<a href=javascript:>4</a>
</div>
</div>
</div>
<div class=comments_holder>
<div class=comments_holder_inner>
<div class=comments_loader>&nbsp;</div>
<ul class="comments_holder_ul latest">
</ul>
</div>
</div>
<div class="more_comments_btn_holder dn"> <span class=more_comments_btn>সব মন্তব্য</span></div>
<div class="comment_closed dn">
<br/>
<p align=center>ইহাতে মন্তব্য প্রদান বন্ধ রয়েছে</p>
</div>
</div>
</div>
</div>
<script>
				var reply_form_builded = '<div class="reply_form_div">\
					<form name="reply_form" action="">\
						<input type="hidden" name="fk_content_id" value="1574390" />\
						<input type="hidden" name="parent" value="0" />\
						<input type="hidden" name="label_depth" value="0" />\
						<div class="textarea_holder comment_input input_wrap">\
							<textarea class="textarea jadewits_keyboard" name="comment" rows="4" cols="40"></textarea>\
						</div>\
						<div class="text_holder">আপনার পরিচয় গোপন রাখতে   <label><input class="checkbox" type="checkbox" name="hidden_name" id="hidden_name" value="1"> এখানে ক্লিক করুন।</label> <br> আমি <a target="_blank" href="http://www.prothomalo.com/user-terms-and-conditions">নীতিমালা</a> মেনে মন্তব্য করছি।</div>\
						<div class="input_wrap"><input type="button" class="button_light reply_submit" name="jadewits_insert_update" value="পাঠিয়ে দিন"></div>\
						<div class="comment_message"></div>\
					</form>\
				</div>';
			</script>
</div>
<script>
		
			$('#jw_comments_order_by').change(function(e) {
				if( $(this).val() == 'new' ){
					$('.comments_holder_ul').addClass('latest');
					}
				else{
					$('.comments_holder_ul').removeClass('latest');
					}
				});
			
		
			jw_limit_text_chars({element:'textarea[name=comment]',char_limit:5000,language:'bn'});
			
			function get_comments_first_label(comment_id, comment_status, like_me, dislike_me, user_name, user_profile_link, user_img_link, comment, create_time, content_id, like_count, dislike_count, label_depth,client_device){
				comments_html = '';
				reply = '';
				share = '';
				if(comment_status == 'published' && label_depth=='0'){
					reply = "<div class='reply_button'><a rel='1' class='reply_comment' id='reply_id_"+comment_id+"'>জবাব</a></div>";
				}
				else if(comment_status == 'pending' ){
					reply = "<div class='reply_button'>অপেক্ষমান</div>";
					}
				if(like_me == 1 )	like_class = 'liked_this';
					else like_class = 'like_count';
					
				if(dislike_me == 1 )	dislike_class = 'disliked_this';
					else dislike_class = 'dislike_count';
	
				if(user_name == 'hidden'){
					get_user_name = "নাম প্রকাশে অনিচ্ছুক";
					get_user_profile_image_link = '';
				}
				else {
					get_user_profile_image_link = "<img height='50' width='50' src='"+user_profile_link+"' alt='User Picture'/>";
					get_user_name = user_name;
				}
				create_time = languageNumber(create_time,'bn');
				comments_html = comments_html + "<li id='commentp_"+comment_id+"'><i id='comment_"+comment_id+"' class='fake_ha'></i>\
					<div class='individual_comment'>\
						<div class='comment_user_info'></div>\
						<div class='info_right'>\
							<div class='info'>\
								<a class='user_images' href='javascript:'>"+get_user_profile_image_link+"</a>\
								<a class=\"uname\" href='javascript:'>"+get_user_name+"</a>\
							</div>\
							<div class='comment_portion'>\
								<p>"+comment+"</p>\
							</div>\
							<div class=\"comment_bottom\">\
								"+reply+"\
								<div class='comment_data'>\
									<div class='comment_data_each'>\
										<a title='Like' data-type='like' data-comment-id='"+comment_id+"' data-content-id='"+content_id+"' class='like_dislike like_btn "+like_class+"'  href='javascript:'></a>\
										<span id='like_comment_"+comment_id+"'>"+like_count+"</span>\
									</div>\
									<div class='comment_data_each'>\
										<a title='Dislike' data-type='dislike' data-comment-id='"+comment_id+"' data-content-id='"+content_id+"' class='like_dislike dislike_btn "+dislike_class+"' href='javascript:'></a>\
										<span id='dislike_comment_"+comment_id+"'>"+dislike_count+"</span>\
									</div>\
								</div>\
								<div class='comment_share social_shares zoom0_60 roundicons' \
									data-show='' \
									data-hide='facebook,twitter,googlePlus' \
									data-title='"+ get_user_name +" commented on " + jw_meta_title + "' \
									data-url='"+jw_meta_url+"#comment_"+comment_id+"' \
									data-description='"+comment+ "'></div> \
							</div>\
						</div>";
		comments_html = comments_html + "</li>"; 	
		return 	comments_html;
	}
			//load comments
			$.ajax({
				cache:false,
				type: 'post',
				url: '/api/comments/get_comments_json/?content_id=1574390',
				dataType:'json',
				data: '',
				success: function(reply_data){
					if(reply_data['error']){
						$('.comments_holder').html('পাওয়া যায়নি');
					}else{
						//$('.comments_holder').html(reply_data); return false;
						var data_array = reply_data;
						var has_comment = false;

						for (var key in data_array) {
							has_comment = true;
								if(data_array[key]['parent']=='0'){
									comm = get_comments_first_label(data_array[key]['comment_id'], data_array[key]['comment_status'], data_array[key]['like_me'], data_array[key]['dislike_me'], data_array[key]['commenter_name'], data_array[key]['commenter_image'], data_array[key]['commenter_profile_link'], data_array[key]['comment'], data_array[key]['create_time'] , data_array[key]['content_id'], data_array[key]['like_count'] , data_array[key]['dislike_count'], data_array[key]['label_depth'], data_array[key]['device']);
										$('.comments_holder_ul').append(comm);
								}else{
									
									parent_li = "commentp_"+data_array[key]['parent'];
									comm = get_comments_first_label(data_array[key]['comment_id'], data_array[key]['comment_status'], data_array[key]['like_me'], data_array[key]['dislike_me'], data_array[key]['commenter_name'], data_array[key]['commenter_image'], data_array[key]['commenter_profile_link'], data_array[key]['comment'], data_array[key]['create_time'] , data_array[key]['content_id'], data_array[key]['like_count'] , data_array[key]['dislike_count'], data_array[key]['label_depth'], data_array[key]['device']);
									
									if( $("#"+parent_li).has("ul").length ){
										$("#"+parent_li+" ul").append(comm);
									}
									else{
											$("#"+parent_li).append('<ul>'+comm+'</ul>');
										}
								}
							}
							
							
						$('.comments_holder .comments_loader').hide();
						
						
						if( !(1) ){
							$('.reply_button').hide();
							$('.reply_comment').hide();
							if( !has_comment ){
								//no comments found also the commenting is close hide full comment section
								$('#comments').hide();
								}
							}
						
						if( has_comment ){
							$('.discussion_toolbar_container').show();
							}
						
						//now scroll to comment position if there is a # link in url
						var has_hash_link = window.location.href.split('#');
						if( has_hash_link[1] ){
							$('.comments_holder').css({height:'auto'}); $('.more_comments_btn_holder').hide();
							window.location.href =  has_hash_link[0] + '#' + has_hash_link[1];
							}
							
						if( $('.comments_holder').height() < $('.comments_holder_inner').height() ){
							$('.more_comments_btn_holder').show();
							$('.more_comments_btn').click(function(e) {
								
								if( $('.comments_holder').height() < $('.comments_holder_inner').height() ){
									$('.comments_holder').css({height:'auto'}); $('.more_comments_btn_holder').hide();
									//$('.comments_holder').css({height:($('.comments_holder').height()+500)+'px'});
									}
								if( $('.comments_holder').height() > $('.comments_holder_inner').height() ){
									$('.more_comments_btn_holder').hide();
									$('.comments_holder').css({height:'auto'});
									}
								});
							}
						else{
							$('.comments_holder').css({height:'auto'});
							}
						$('.social_shares' ).trigger('jadewitsShare');

					}
					
					if( !__is_jadewits_user_logged_in ){
						$('.reply_button').hide();
						}
					},
				error: function(){
					$('.comments_holder').html('নেটওয়ার্ক ত্রুটি');
					}
				});
		
			if( __is_jadewits_user_logged_in && 1 ){
				$('#write_comments').show();
				
				$('.comment_submit').click(function() {
						var theForm = $('#comment_form');
						if(!$('[name="comment"]',theForm).val()){ 
							alert('Please write your comment.'); 
							return false;
							}
						var data = theForm.serialize();
						
						$(":input",theForm).attr("disabled", true);
						$.ajax({
								cache:false,
								type: 'post',
								url: '/api/comments/comments_process_json/',
								data: data,
								dataType:'json',
								//beforeSend: function(){},
								success: function(reply_data){
										if(reply_data['error'])
												$('.comment_message',theForm).html(reply_data['error']);
										else{
												comm = get_comments_first_label(reply_data['success']['comment_id'], reply_data['success']['comment_status'], reply_data['success']['like_me'], reply_data['success']['dislike_me'], reply_data['success']['commenter_name'], reply_data['success']['commenter_image'], reply_data['success']['commenter_profile_link'], reply_data['success']['comment'], reply_data['success']['create_time'] , reply_data['success']['content_id'], reply_data['success']['like_count'] , reply_data['success']['dislike_count'], reply_data['success']['label_depth'], reply_data['success']['device']);
											
												$('.comment_message',theForm).html('মন্তব্য করার জন্য ধন্যবাদ, আপনার মন্তব্যটি প্রকাশের জন্য অপেক্ষমান');
												$('[name=comment]',theForm).val('');
												$('.comments_holder_ul').append(comm);
											}
										$(":input",theForm).attr("disabled", false);
									},
								error: function(){
									$('.comment_message',theForm).html('অপ্রত্যাশিত ভুল।');
									$(":input",theForm).attr("disabled", false);
									}
							});
				  return false;
				});
				
				$('.reply_submit').live('click', function() {
						var theForm = $(this).parent().parent();
						if(!$('[name="comment"]',theForm).val()){ 
							alert('Please write your comment.'); 
							return false;
							}
						var data = theForm.serialize();
						$(":input",theForm).attr("disabled", true);
						$.ajax({
								cache:false,
								type: 'post',
								url: '/api/comments/comments_process_json/',
								dataType:'json',
								data: data,
								success: function(reply_data){
										if( reply_data['success'] ){

															parent_li = "commentp_"+reply_data['success']['parent'];
															comm = get_comments_first_label(reply_data['success']['comment_id'], reply_data['success']['comment_status'], reply_data['success']['like_me'], reply_data['success']['dislike_me'], reply_data['success']['commenter_name'], reply_data['success']['commenter_image'], reply_data['success']['commenter_profile_link'], reply_data['success']['comment'], reply_data['success']['create_time'] , reply_data['success']['content_id'], reply_data['success']['like_count'] , reply_data['success']['dislike_count'], reply_data['success']['label_depth'], reply_data['success']['device']);
															if( $("#"+parent_li).has("ul").length ){
																	$("#"+parent_li+" ul").prepend(comm);
															}
															else{
																	$("#"+parent_li).append('<ul>'+comm+'</ul>');
																}
										
											$('.comment_message',theForm).html('');
											$('[name=comment]',theForm).val('');
											theForm.parent().hide();
											}
										else if(reply_data['error']){
											$('.comment_message',theForm).html(reply_data['error']);
										}else{
											$('.comment_message',theForm).html('অপ্রত্যাশিত ভুল।');
											}
										$(":input",theForm).attr("disabled", false);	
									},
								error:function(){
									$('.comment_message',theForm).html('অপ্রত্যাশিত ভুল।');
									$(":input",theForm).attr("disabled", false);	
									}
							});
					
				  return false;
				});
				
				$('.reply_comment').live('click', function(){
						var reply_id = $(this).attr('id');
						var label_depth = $(this).attr('rel')
						var comment_id = reply_id.replace('reply_id_','');
						
						var container = $('#'+reply_id).parent().parent().parent();
						var alreadyhasone = $('.reply_form_div',container);
						
						//hide others first
						$('.reply_form_div').hide();
						
						if( alreadyhasone.length ){
							alreadyhasone.show();
							}
						else{
							container.append( reply_form_builded );
							var builded_reply_form = $('.reply_form_div',container);
							$('[name=parent]',builded_reply_form).val(comment_id);
							$('[name=label_depth]',builded_reply_form).val(label_depth);
							}
					});
					
				$('.like_dislike').live('click', function(){
												
						var like_dislike = $(this).data('type');
						var fk_content_id = $(this).data('content-id');
						var comment_id = $(this).data('comment-id');
						var the_node = $(this);
						data = '&comment_id='+comment_id+'&like_dislike='+like_dislike+'&fk_content_id='+fk_content_id+'&content_link='+encodeURIComponent(window.location.href.split('#')[0]);
						
						if( like_dislike == 'like' )
						{
							if( the_node.hasClass('liked_this') )
								return;
						}
						if(like_dislike =='dislike')
						{
							if( the_node.hasClass('disliked_this') )
								return;
						}
						$.ajax({
								cache:false,
								type: 'post',
								url: '/api/comments/like_dislike_comment/',
								dataType:'json',
								data: data,
								//beforeSend: function(){}	
								success: function(reply_data){ 
									if(reply_data['success']){
										$('#like_comment_'+comment_id).html(reply_data['success']['liked']);
										$('#dislike_comment_'+comment_id).html(reply_data['success']['disliked']);
										
										if(like_dislike =='like'){
											the_node.removeClass('like_count').addClass('liked_this');
											//remove status of dislike button
											$('a.dislike_btn',the_node.parent().parent()).removeClass('disliked_this').addClass('dislike_count');
											}
										
										if(like_dislike == 'dislike'){
											the_node.removeClass('dislike_count').addClass('disliked_this');
											//remove status of like button
											$('a.like_btn',the_node.parent().parent()).removeClass('liked_this').addClass('like_count');
											}
											
										}
										if(reply_data['error'])
										{
											alert(reply_data['error']);	
										}
									},
								error: function(){
									//alert(reply_data['error']);
									}
							});
					});	
				}
			else if( __is_jadewits_user_logged_in && !(1) ){
				$('.reply_button').hide();
				$('.reply_comment').hide();
				//$('.comment_closed').show();
				}
			else{
				$('.login_prompt').show();
				$('.reply_button').hide();
				$('.like_dislike').live('click',function(){
					if( confirm('Please login to ' + $(this).data('type') + ' comment.') ){
						window.location.href = '#login_prompt';
						}
					});
				}
			</script>
</div></div><div id=widget_74146 class="widget_color_ widget_wrap"><div class="detail_next_previous_content  widget">	<div class=content_next_prev>
<div class="prev content_holder">
<span class=t_btn></span>
<div class=content_inner>
<div class=contents>
<div class="each col_in 
			has_image 
			image_left 
			content_capability_blog 
			content_type_article 
			responsive_image_hide_			 
			 
			 
						 
		">
<a class=link_overlay href="/bangladesh/article/1574384/%E2%80%98%E0%A6%AD%E0%A7%81%E0%A6%B2%E2%80%99-%E0%A6%B8%E0%A7%8D%E0%A6%AC%E0%A7%80%E0%A6%95%E0%A6%BE%E0%A6%B0-%E0%A6%95%E0%A6%B0%E0%A6%BE%E0%A7%9F-%E0%A6%A1.-%E0%A6%95%E0%A6%BE%E0%A6%AE%E0%A6%BE%E0%A6%B2%E0%A6%95%E0%A7%87-%E0%A6%A7%E0%A6%A8%E0%A7%8D%E0%A6%AF%E0%A6%AC%E0%A6%BE%E0%A6%A6-%E0%A6%A4%E0%A6%A5%E0%A7%8D%E0%A6%AF%E0%A6%AE%E0%A6%A8%E0%A7%8D%E0%A6%A4%E0%A7%8D%E0%A6%B0%E0%A7%80%E0%A6%B0"></a>
<div class=image>
<noscript id=ari-image-741461574384 data-ari="{&quot;path&quot;:&quot;media\/2019\/01\/13\/7839d0dd268e453ab4596db0f3f5da88-5c3ae9170e37b.jpg?jadewits_media_id=1409275&quot;,&quot;ratio&quot;:[16,9],&quot;alt&quot;:&quot;\u2018\u09ad\u09c1\u09b2\u2019 \u09b8\u09cd\u09ac\u09c0\u0995\u09be\u09b0 \u0995\u09b0\u09be\u09df \u09a1. \u0995\u09be\u09ae\u09be\u09b2\u0995\u09c7 \u09a7\u09a8\u09cd\u09af\u09ac\u09be\u09a6 \u09a4\u09a5\u09cd\u09af\u09ae\u09a8\u09cd\u09a4\u09cd\u09b0\u09c0\u09b0&quot;}">
<img src="//paloimages.prothom-alo.com/contents/cache/images/400x225x1/uploads/media/2019/01/13/7839d0dd268e453ab4596db0f3f5da88-5c3ae9170e37b.jpg?jadewits_media_id=1409275" alt="‘ভুল’ স্বীকার করায় ড. কামালকে ধন্যবাদ তথ্যমন্ত্রীর"/>
</noscript>
<script data-id=ari-image-741461574384>
								jwARI.fetch( $( '#ari-image-741461574384' ) );
							</script>
<span class=content_type></span>
</div>
<div class="info ">
<h2 class=title_holder>
<span class=title>‘ভুল’ স্বীকার করায় ড. কামালকে ধন্যবাদ তথ্যমন্ত্রীর</span>
</h2>
<div class=additional>
</div>
</div>
</div>
</div>
<div class=foot>আগের সংবাদ</div>
</div>
</div>
<div class="content_holder next">
<span class=t_btn></span>
<div class=content_inner>
<div class=contents>
<div class="each col_in 
			has_image 
			image_left 
			content_capability_blog 
			content_type_article 
			responsive_image_hide_			 
			 
			 
						 
		">
<a class=link_overlay href="/bangladesh/article/1574392/%E0%A6%B8%E0%A6%B6%E0%A6%B8%E0%A7%8D%E0%A6%A4%E0%A7%8D%E0%A6%B0-%E0%A6%AC%E0%A6%BE%E0%A6%B9%E0%A6%BF%E0%A6%A8%E0%A7%80%E0%A6%B0-%E0%A6%B6%E0%A6%B9%E0%A7%80%E0%A6%A6%E0%A6%A6%E0%A7%87%E0%A6%B0-%E0%A6%AA%E0%A7%8D%E0%A6%B0%E0%A6%A4%E0%A6%BF-%E0%A6%AA%E0%A7%8D%E0%A6%B0%E0%A6%A7%E0%A6%BE%E0%A6%A8%E0%A6%AE%E0%A6%A8%E0%A7%8D%E0%A6%A4%E0%A7%8D%E0%A6%B0%E0%A7%80%E0%A6%B0"></a>
<div class=image>
<noscript id=ari-image-741461574392 data-ari="{&quot;path&quot;:&quot;media\/2019\/01\/13\/6c025226f2f146fdafcb69939138c6ca-5c3af7d668b65.jpg?jadewits_media_id=1409298&quot;,&quot;ratio&quot;:[16,9],&quot;alt&quot;:&quot;\u09b8\u09b6\u09b8\u09cd\u09a4\u09cd\u09b0 \u09ac\u09be\u09b9\u09bf\u09a8\u09c0\u09b0 \u09b6\u09b9\u09c0\u09a6\u09a6\u09c7\u09b0 \u09aa\u09cd\u09b0\u09a4\u09bf \u09aa\u09cd\u09b0\u09a7\u09be\u09a8\u09ae\u09a8\u09cd\u09a4\u09cd\u09b0\u09c0\u09b0 \u09b6\u09cd\u09b0\u09a6\u09cd\u09a7\u09be&quot;}">
<img src="//paloimages.prothom-alo.com/contents/cache/images/400x225x1/uploads/media/2019/01/13/6c025226f2f146fdafcb69939138c6ca-5c3af7d668b65.jpg?jadewits_media_id=1409298" alt="সশস্ত্র বাহিনীর শহীদদের প্রতি প্রধানমন্ত্রীর শ্রদ্ধা"/>
</noscript>
<script data-id=ari-image-741461574392>
								jwARI.fetch( $( '#ari-image-741461574392' ) );
							</script>
<span class=content_type></span>
</div>
<div class="info ">
<h2 class=title_holder>
<span class=title>সশস্ত্র বাহিনীর শহীদদের প্রতি প্রধানমন্ত্রীর শ্রদ্ধা</span>
</h2>
<div class=additional>
</div>
</div>
</div>
</div>
<div class=foot>পরের সংবাদ</div>
</div>
</div>
</div>
<script>
			/*$('.content_next_prev .t_btn').hover(function(e) {
				$(this).parent().find('.content_inner').toggle(200);
			});*/
		</script>
</div></div></div></div><div id=div_74136 class="p_c  specl_ad_comments   _col"><div class=inner><div id=widget_75456 class="widget_color_ widget_wrap"><div class="widget_text  widget">	<div class="widget_text_inner aunqur">
<div class=content><div class=common_google_ads>
<div id=div-gpt-ad-10691-16>
<script>
    googletag.cmd.push(function() { googletag.display('div-gpt-ad-10691-16'); });
  </script>
</div>
</div></div>
</div>
</div></div></div></div></div></div><div id=wrapper_52363 class="wrapper   container_fixed_height container_white_bg container_top_padding "><div class=inner><div id=div_52364 class="p_p     _col"><div class=inner><div id=widget_52365 class="widget_color_ widget_wrap"><div class="contents_listing  widget">	<div class="contents  summery_view col_articles 
			shaded_bg 
						column_view 
			">
<div class=row><div class="col col4">	<div class="each col_in 
			has_image 
			image_top 
			content_capability_blog 
			content_type_article 
			responsive_image_hide_			 
			 
			 
						 
		">
<a class=link_overlay href="/bangladesh/article/1574390/%E0%A6%B8%E0%A7%81%E0%A6%AC%E0%A6%B0%E0%A7%8D%E0%A6%A3%E0%A6%9A%E0%A6%B0%E0%A7%87-%E0%A6%A7%E0%A6%B0%E0%A7%8D%E0%A6%B7%E0%A6%A3%E0%A7%87%E0%A6%B0-%E0%A6%98%E0%A6%9F%E0%A6%A8%E0%A6%BE%E0%A6%B0-%E0%A6%B8%E0%A6%99%E0%A7%8D%E0%A6%97%E0%A7%87-%E0%A6%AD%E0%A7%8B%E0%A6%9F%E0%A7%87%E0%A6%B0-%E0%A6%B8%E0%A6%AE%E0%A7%8D%E0%A6%AA%E0%A6%B0%E0%A7%8D%E0%A6%95-%E0%A6%AA%E0%A6%BE%E0%A7%9F%E0%A6%A8%E0%A6%BF"></a>
<div class=image>
<noscript id=ari-image-523651574390 data-ari="{&quot;path&quot;:&quot;media\/2018\/03\/18\/cc1107dbb1c246a9093a95ef8df7e78e-5aae1122a6fb1.jpg?jadewits_media_id=1199871&quot;,&quot;ratio&quot;:[16,9],&quot;alt&quot;:&quot;\u09b8\u09c1\u09ac\u09b0\u09cd\u09a3\u099a\u09b0\u09c7 \u09a7\u09b0\u09cd\u09b7\u09a3\u09c7\u09b0 \u0998\u099f\u09a8\u09be\u09b0 \u09b8\u0999\u09cd\u0997\u09c7 \u09ad\u09cb\u099f\u09c7\u09b0 \u09b8\u09ae\u09cd\u09aa\u09b0\u09cd\u0995 \u09aa\u09be\u09df\u09a8\u09bf \u09ae\u09be\u09a8\u09ac\u09be\u09a7\u09bf\u0995\u09be\u09b0 \u0995\u09ae\u09bf\u09b6\u09a8&quot;}">
<img src="//paloimages.prothom-alo.com/contents/cache/images/400x225x1/uploads/media/2018/03/18/cc1107dbb1c246a9093a95ef8df7e78e-5aae1122a6fb1.jpg?jadewits_media_id=1199871" alt="সুবর্ণচরে ধর্ষণের ঘটনার সঙ্গে ভোটের সম্পর্ক পায়নি মানবাধিকার কমিশন"/>
</noscript>
<script data-id=ari-image-523651574390>
								jwARI.fetch( $( '#ari-image-523651574390' ) );
							</script>
<span class=content_type></span>
</div>
<div class="info has_ai">
<h2 class=title_holder>
<span class=title>সুবর্ণচরে ধর্ষণের ঘটনার সঙ্গে ভোটের সম্পর্ক পায়নি মানবাধিকার কমিশন</span>
</h2>
<div class=summery>
জাতীয় মানবাধিকার কমিশনের তথ্যানুসন্ধান প্রতিবেদন বলছে, সুবর্ণচরে ধর্ষণের...
</div>
<div class=additional>
<a class="category aitm" href="/bangladesh">বাংলাদেশ</a>
</div>
</div>
</div>
</div><div class="col col4">	<div class="each col_in 
			has_image 
			image_top 
			content_capability_blog 
			content_type_article 
			responsive_image_hide_			 
			 
			 
						 
		">
<a class=link_overlay href="/economy/article/1574391/%E0%A6%95%E0%A6%BE%E0%A6%9C%E0%A7%87-%E0%A6%A8%E0%A6%BE-%E0%A6%AB%E0%A6%BF%E0%A6%B0%E0%A6%B2%E0%A7%87-%E0%A6%95%E0%A6%BE%E0%A6%B0%E0%A6%96%E0%A6%BE%E0%A6%A8%E0%A6%BE-%E0%A6%AC%E0%A6%A8%E0%A7%8D%E0%A6%A7-%E0%A6%AC%E0%A6%BF%E0%A6%9C%E0%A6%BF%E0%A6%8F%E0%A6%AE%E0%A6%87%E0%A6%8F"></a>
<div class=image>
<noscript id=ari-image-523651574391 data-ari="{&quot;path&quot;:&quot;media\/2017\/03\/12\/94c976fa9538c8cc6302d95660422bce-58c4c8b60a10a.jpg?jadewits_media_id=764071&quot;,&quot;ratio&quot;:[16,9],&quot;alt&quot;:&quot;\u0995\u09be\u099c\u09c7 \u09a8\u09be \u09ab\u09bf\u09b0\u09b2\u09c7 \u0995\u09be\u09b0\u0996\u09be\u09a8\u09be \u09ac\u09a8\u09cd\u09a7: \u09ac\u09bf\u099c\u09bf\u098f\u09ae\u0987\u098f&quot;}">
<img src="//paloimages.prothom-alo.com/contents/cache/images/400x225x1/uploads/media/2017/03/12/94c976fa9538c8cc6302d95660422bce-58c4c8b60a10a.jpg?jadewits_media_id=764071" alt="কাজে না ফিরলে কারখানা বন্ধ: বিজিএমইএ"/>
</noscript>
<script data-id=ari-image-523651574391>
								jwARI.fetch( $( '#ari-image-523651574391' ) );
							</script>
<span class=content_type></span>
</div>
<div class="info has_ai">
<h2 class=title_holder>
<span class=title>কাজে না ফিরলে কারখানা বন্ধ: বিজিএমইএ</span>
</h2>
<div class=summery>
পোশাকশ্রমিকেরা কাজে না ফিরলে আগামীকাল সোমবার থেকে অনির্দিষ্টকালের জন্য...
</div>
<div class=additional>
<a class="category aitm" href="/economy">অর্থনীতি</a>
</div>
</div>
</div>
</div><div class="col col4">	<div class="each col_in 
			has_image 
			image_top 
			content_capability_blog 
			content_type_article 
			responsive_image_hide_			 
			 
			 
						 
		">
<a class=link_overlay href="/education/article/1574389/%E0%A6%9B%E0%A6%BE%E0%A6%A4%E0%A7%8D%E0%A6%B0%E0%A6%B2%E0%A7%80%E0%A6%97%E2%80%93%E0%A6%B6%E0%A6%BF%E0%A6%95%E0%A7%8D%E0%A6%B7%E0%A6%95-%E0%A6%B8%E0%A6%AE%E0%A6%BF%E0%A6%A4%E0%A6%BF-%E0%A6%AE%E0%A7%81%E0%A6%96%E0%A7%8B%E0%A6%AE%E0%A7%81%E0%A6%96%E0%A6%BF-%E0%A6%85%E0%A6%AC%E0%A6%B8%E0%A7%8D%E0%A6%A5%E0%A6%BE%E0%A6%A8%E0%A7%87"></a>
<div class=image>
<noscript id=ari-image-523651574389 data-ari="{&quot;path&quot;:&quot;media\/2019\/01\/13\/4a0989bfcfcc1a7583e7efe5f5357475-5c3aede14d763.jpg?jadewits_media_id=1409288&quot;,&quot;ratio&quot;:[16,9],&quot;alt&quot;:&quot;\u099b\u09be\u09a4\u09cd\u09b0\u09b2\u09c0\u0997\u2013\u09b6\u09bf\u0995\u09cd\u09b7\u0995 \u09b8\u09ae\u09bf\u09a4\u09bf \u09ae\u09c1\u0996\u09cb\u09ae\u09c1\u0996\u09bf \u0985\u09ac\u09b8\u09cd\u09a5\u09be\u09a8\u09c7&quot;}">
<img src="//paloimages.prothom-alo.com/contents/cache/images/400x225x1/uploads/media/2019/01/13/4a0989bfcfcc1a7583e7efe5f5357475-5c3aede14d763.jpg?jadewits_media_id=1409288" alt="ছাত্রলীগ–শিক্ষক সমিতি মুখোমুখি অবস্থানে"/>
</noscript>
<script data-id=ari-image-523651574389>
								jwARI.fetch( $( '#ari-image-523651574389' ) );
							</script>
<span class=content_type></span>
</div>
<div class="info has_ai">
<h2 class=title_holder>
<span class=subtitle>যশোর প্রযুক্তি বিশ্ববিদ্যালয়</span>	<span class=title>ছাত্রলীগ–শিক্ষক সমিতি মুখোমুখি অবস্থানে</span>
</h2>
<div class=summery>
জাতীয় সংসদ নির্বাচন উপলক্ষে যশোর বিজ্ঞান ও প্রযুক্তি বিশ্ববিদ্যালয় ক্যাম্পাসে...
</div>
<div class=additional>
<a class="category aitm" href="/education">শিক্ষা</a>
</div>
</div>
</div>
</div><div class="col col4">	<div class="each col_in 
			has_image 
			image_top 
			content_capability_blog 
			content_type_article 
			responsive_image_hide_			 
			 
			 
						 
		">
<a class=link_overlay href="/international/article/1574393/%E0%A6%85%E0%A6%B8%E0%A7%8D%E0%A6%A4%E0%A7%8D%E0%A6%B0%E0%A7%8B%E0%A6%AA%E0%A6%9A%E0%A6%BE%E0%A6%B0-%E0%A6%95%E0%A6%95%E0%A7%8D%E0%A6%B7%E0%A7%87-%E0%A6%98%E0%A7%81%E0%A6%AE%E0%A6%BF%E0%A7%9F%E0%A7%87%E0%A6%93-%E0%A6%A8%E0%A6%BE%E0%A7%9F%E0%A6%95-%E0%A6%8F%E0%A6%95-%E0%A6%9A%E0%A6%BF%E0%A6%95%E0%A6%BF%E0%A7%8E%E0%A6%B8%E0%A6%95"></a>
<div class=image>
<noscript id=ari-image-523651574393 data-ari="{&quot;path&quot;:&quot;media\/2019\/01\/13\/0e4fea944da72d9fe9191a08c89c67cf-5c3af2a6e1aa0.jpg?jadewits_media_id=1409295&quot;,&quot;ratio&quot;:[16,9],&quot;alt&quot;:&quot;\u0985\u09b8\u09cd\u09a4\u09cd\u09b0\u09cb\u09aa\u099a\u09be\u09b0 \u0995\u0995\u09cd\u09b7\u09c7 \u0998\u09c1\u09ae\u09bf\u09df\u09c7\u0993 \u09a8\u09be\u09df\u0995 \u098f\u0995 \u099a\u09bf\u0995\u09bf\u09ce\u09b8\u0995&quot;}">
<img src="//paloimages.prothom-alo.com/contents/cache/images/400x225x1/uploads/media/2019/01/13/0e4fea944da72d9fe9191a08c89c67cf-5c3af2a6e1aa0.jpg?jadewits_media_id=1409295" alt="অস্ত্রোপচার কক্ষে ঘুমিয়েও নায়ক এক চিকিৎসক"/>
</noscript>
<script data-id=ari-image-523651574393>
								jwARI.fetch( $( '#ari-image-523651574393' ) );
							</script>
<span class=content_type></span>
</div>
<div class="info has_ai">
<h2 class=title_holder>
<span class=subtitle>বিচিত্র</span>	<span class=title>অস্ত্রোপচার কক্ষে ঘুমিয়েও নায়ক এক চিকিৎসক</span>
</h2>
<div class=summery>
অস্ত্রোপচারের মাঝপথে রোগীকে টেবিলে রেখে সেখানেই ঘুমিয়ে গিয়েছিলেন চিকিৎসক। সেই...
</div>
<div class=additional>
<a class="category aitm" href="/international">আন্তর্জাতিক</a>
</div>
</div>
</div>
</div></div>	</div>
</div></div><div id=widget_69331 class="widget_color_ widget_wrap"><div class="widget_text  widget">	<div class="widget_text_inner aunqur">
<div class=content><style>
.special_bg_for_list{
 background: #ceecd2;
padding: 14px 16px; 
}
ul.special_bg_for_list li{
 padding-bottom: 8px;
}

</style></div>
</div>
</div></div></div></div></div></div><div id=wrapper_70356 class="wrapper   container_fixed_height container_white_bg container_bottom_padding "><div class=inner><div id=div_70361 class="p_p     _col"><div class=inner><div id=widget_97341 class="widget_color_ widget_wrap"><div class="widget_text  widget">	<div class="widget_text_inner aunqur">
<div class=content><style>
.palo_elec_wrapper{
    border: 1px solid #ffa809;
    margin: 24px auto;
    background: #fff700;
}
.palo_elec_wrapper:hover{
	background: #feffa4;
}
.palo_elec_wrapper a{
    display: table;
    overflow: hidden;
    padding: 8px 16px;
	text-decoration:none
}
.palo_elec_wrapper img{
    width: 64px;
    float: left;
    margin-right: 28px;
}
.palo_elec_wrapper span{
    line-height: 32px;
    color: #029e1c;
    font-weight: bold;
    font-size: 22px;
    display: table-cell;
    vertical-align: middle;
    padding-left: 16px;
}
</style>
<script type="application/javascript">
$(document).ready(function(){
if($(".topic_list").is(':contains("একাদশ সংসদ নির্বাচন")')){
		$("article").append('<a href="https://election.prothomalo.com/?utm_source=PALO_In-Article&utm_medium=Clicks&utm_campaign=Election_Dec-18" target="_blank"><img src="https://paloimages.prothom-alo.com/contents/cache/images/689x151x1/uploads/media/2018/11/29/5dc07744be7f4f75667865369e95eff8-5c0002e076988.png" alt="জাতীয় সংসদ নির্বাচন ২০১৮"></a>');
	}
	if($(".topic_list").is(':contains("সিলেট সিটি করপোরেশন")')){
		$("article").append('<div class="palo_elec_wrapper"><a href="http://www.prothomalo.com/election-sylhet" target="_blank"><img src="//paimages.prothom-alo.com/contents/uploads/media/2018/07/23/cf6e0799dd7ee064452be250e36a52d9-5b5583324cd52.png" alt="সিলেট সিটি করপোরেশন নির্বাচন"><span>এক নজরে সিলেট সিটি করপোরেশন নির্বাচন</span></a></div>');
	}
	
	if($(".topic_list").is(':contains("রাজশাহী সিটি করপোরেশন")')){
		$("article").append('<div class="palo_elec_wrapper"><a href="http://www.prothomalo.com/election-rajshahi" target="_blank"><img src="//paimages.prothom-alo.com/contents/uploads/media/2018/07/23/7e7a54f232353c2412799b8bb5b8e1c7-5b5583e95c88c.png" alt="রাজশাহী সিটি করপোরেশন নির্বাচন"><span>এক নজরে রাজশাহী সিটি করপোরেশন নির্বাচন</span></a></div>');
	}
	
	if($(".topic_list").is(':contains("বরিশাল সিটি করপোরেশন")')){
		$("article").append('<div class="palo_elec_wrapper"><a href="http://www.prothomalo.com/election-barishal" target="_blank"><img src="//paimages.prothom-alo.com/contents/uploads/media/2018/07/23/e0c5cd0c568c25380f2bafc940d4b4c6-5b5583ffdf62c.png" alt="বরিশাল সিটি করপোরেশন নির্বাচন"><span>এক নজরে বরিশাল সিটি করপোরেশন নির্বাচন</span></a></div>');
	}
});
</script></div>
</div>
</div></div><div id=widget_70406 class="widget_color_ widget_wrap"><div class="widget_text  widget">	<div class="widget_text_inner aunqur">
<div class=content><div class=common_google_ads>
<div id=div-gpt-ad-10691-9>
<script>
    googletag.cmd.push(function() { googletag.display('div-gpt-ad-10691-9'); });
  </script>
</div>
</div>
<div class=Special_ad_b2> </div></div>
</div>
</div></div><div id=widget_70366 class="widget_color_ widget_wrap"><div class="contents_listing  widget">	<div class="contents  summery_view col_articles 
			shaded_bg 
						column_view 
			">
<div class=row><div class="col col4">	<div class="each col_in 
			has_image 
			image_top 
			content_capability_blog 
			content_type_article 
			responsive_image_hide_			 
			 
			 
						 
		">
<a class=link_overlay href="/bangladesh/article/1574381/%E0%A6%86%E0%A6%AC%E0%A6%BE%E0%A6%B0%E0%A6%93-%E0%A6%B8%E0%A6%82%E0%A6%B2%E0%A6%BE%E0%A6%AA%E0%A7%87-%E0%A6%AC%E0%A6%B8%E0%A6%AC%E0%A7%87%E0%A6%A8-%E0%A6%AA%E0%A7%8D%E0%A6%B0%E0%A6%A7%E0%A6%BE%E0%A6%A8%E0%A6%AE%E0%A6%A8%E0%A7%8D%E0%A6%A4%E0%A7%8D%E0%A6%B0%E0%A7%80-%E0%A6%95%E0%A6%BE%E0%A6%A6%E0%A7%87%E0%A6%B0"></a>
<div class=image>
<noscript id=ari-image-703661574381 data-ari="{&quot;path&quot;:&quot;media\/2019\/01\/02\/ee788e8137f1138c3a313a0e353e1acb-5c2ca65265a15.jpg?jadewits_media_id=1406882&quot;,&quot;ratio&quot;:[16,9],&quot;alt&quot;:&quot;\u0986\u09ac\u09be\u09b0\u0993 \u09b8\u0982\u09b2\u09be\u09aa\u09c7 \u09ac\u09b8\u09ac\u09c7\u09a8 \u09aa\u09cd\u09b0\u09a7\u09be\u09a8\u09ae\u09a8\u09cd\u09a4\u09cd\u09b0\u09c0: \u0995\u09be\u09a6\u09c7\u09b0&quot;}">
<img src="//paloimages.prothom-alo.com/contents/cache/images/400x225x1/uploads/media/2019/01/02/ee788e8137f1138c3a313a0e353e1acb-5c2ca65265a15.jpg?jadewits_media_id=1406882" alt="আবারও সংলাপে বসবেন প্রধানমন্ত্রী: কাদের"/>
</noscript>
<script data-id=ari-image-703661574381>
								jwARI.fetch( $( '#ari-image-703661574381' ) );
							</script>
<span class=content_type></span>
</div>
<div class="info has_ai">
<h2 class=title_holder>
<span class=title>আবারও সংলাপে বসবেন প্রধানমন্ত্রী: কাদের</span>
</h2>
<div class=summery>
আওয়ামী লীগের সাধারণ সম্পাদক ওবায়দুল কাদের বলেছেন, একাদশ জাতীয় সংসদ নির্বাচনের...
</div>
<div class=additional>
<a class="category aitm" href="/bangladesh">বাংলাদেশ</a>
</div>
</div>
</div>
</div><div class="col col4">	<div class="each col_in 
			has_image 
			image_top 
			content_capability_blog 
			content_type_article 
			responsive_image_hide_			 
			 
			 
						 
		">
<a class=link_overlay href="/opinion/article/1574376/%E0%A6%96%E0%A6%9A%E0%A6%96%E0%A6%9A-%E0%A6%89%E0%A6%B8%E0%A6%95%E0%A6%BE%E0%A6%A8%E0%A6%BF-%E0%A6%86%E0%A6%B0-%E0%A6%A8%E0%A6%BE%E0%A6%95%E0%A7%87-%E0%A6%B7%E0%A7%9C%E0%A6%AF%E0%A6%A8%E0%A7%8D%E0%A6%A4%E0%A7%8D%E0%A6%B0%E0%A7%87%E0%A6%B0-%E0%A6%97%E0%A6%A8%E0%A7%8D%E0%A6%A7"></a>
<div class=image>
<noscript id=ari-image-703661574376 data-ari="{&quot;path&quot;:&quot;media\/2019\/01\/13\/7c52580a40d31c318747e9087dc3a574-5c3ae33d6e558.jpg?jadewits_media_id=1409263&quot;,&quot;ratio&quot;:[16,9],&quot;alt&quot;:&quot;\u0996\u099a\u0996\u099a \u0989\u09b8\u0995\u09be\u09a8\u09bf \u0986\u09b0 \u09a8\u09be\u0995\u09c7 \u09b7\u09dc\u09af\u09a8\u09cd\u09a4\u09cd\u09b0\u09c7\u09b0 \u0997\u09a8\u09cd\u09a7&quot;}">
<img src="//paloimages.prothom-alo.com/contents/cache/images/400x225x1/uploads/media/2019/01/13/7c52580a40d31c318747e9087dc3a574-5c3ae33d6e558.jpg?jadewits_media_id=1409263" alt="খচখচ উসকানি আর নাকে ষড়যন্ত্রের গন্ধ"/>
</noscript>
<script data-id=ari-image-703661574376>
								jwARI.fetch( $( '#ari-image-703661574376' ) );
							</script>
<span class=content_type></span>
</div>
<div class="info has_ai">
<h2 class=title_holder>
<span class=title>খচখচ উসকানি আর নাকে ষড়যন্ত্রের গন্ধ</span>
</h2>
<div class=summery>
জীবনের দাবি অনেক বেশি। তবু সামান্যটুকু মেটাতে ন্যূনতম শ্রম মজুরি ১৬ হাজার...
</div>
<div class=additional>
<a class="category aitm" href="/opinion">মতামত</a>
</div>
</div>
</div>
</div><div class="col col4">	<div class="each col_in 
			has_image 
			image_top 
			content_capability_blog 
			content_type_article 
			responsive_image_hide_			 
			 
			 
						 
		">
<a class=link_overlay href="/bangladesh/article/1574392/%E0%A6%B8%E0%A6%B6%E0%A6%B8%E0%A7%8D%E0%A6%A4%E0%A7%8D%E0%A6%B0-%E0%A6%AC%E0%A6%BE%E0%A6%B9%E0%A6%BF%E0%A6%A8%E0%A7%80%E0%A6%B0-%E0%A6%B6%E0%A6%B9%E0%A7%80%E0%A6%A6%E0%A6%A6%E0%A7%87%E0%A6%B0-%E0%A6%AA%E0%A7%8D%E0%A6%B0%E0%A6%A4%E0%A6%BF-%E0%A6%AA%E0%A7%8D%E0%A6%B0%E0%A6%A7%E0%A6%BE%E0%A6%A8%E0%A6%AE%E0%A6%A8%E0%A7%8D%E0%A6%A4%E0%A7%8D%E0%A6%B0%E0%A7%80%E0%A6%B0"></a>
<div class=image>
<noscript id=ari-image-703661574392 data-ari="{&quot;path&quot;:&quot;media\/2019\/01\/13\/6c025226f2f146fdafcb69939138c6ca-5c3af7d668b65.jpg?jadewits_media_id=1409298&quot;,&quot;ratio&quot;:[16,9],&quot;alt&quot;:&quot;\u09b8\u09b6\u09b8\u09cd\u09a4\u09cd\u09b0 \u09ac\u09be\u09b9\u09bf\u09a8\u09c0\u09b0 \u09b6\u09b9\u09c0\u09a6\u09a6\u09c7\u09b0 \u09aa\u09cd\u09b0\u09a4\u09bf \u09aa\u09cd\u09b0\u09a7\u09be\u09a8\u09ae\u09a8\u09cd\u09a4\u09cd\u09b0\u09c0\u09b0 \u09b6\u09cd\u09b0\u09a6\u09cd\u09a7\u09be&quot;}">
<img src="//paloimages.prothom-alo.com/contents/cache/images/400x225x1/uploads/media/2019/01/13/6c025226f2f146fdafcb69939138c6ca-5c3af7d668b65.jpg?jadewits_media_id=1409298" alt="সশস্ত্র বাহিনীর শহীদদের প্রতি প্রধানমন্ত্রীর শ্রদ্ধা"/>
</noscript>
<script data-id=ari-image-703661574392>
								jwARI.fetch( $( '#ari-image-703661574392' ) );
							</script>
<span class=content_type></span>
</div>
<div class="info has_ai">
<h2 class=title_holder>
<span class=title>সশস্ত্র বাহিনীর শহীদদের প্রতি প্রধানমন্ত্রীর শ্রদ্ধা</span>
</h2>
<div class=summery>
চতুর্থবারের মতো প্রধানমন্ত্রী হিসেবে দায়িত্ব নেওয়ার পর শেখ হাসিনা বাংলাদেশ...
</div>
<div class=additional>
<a class="category aitm" href="/bangladesh">বাংলাদেশ</a>
</div>
</div>
</div>
</div><div class="col col4">	<div class="each col_in 
			has_image 
			image_top 
			content_capability_blog 
			content_type_article 
			responsive_image_hide_			 
			 
			 
						 
		">
<a class=link_overlay href="/northamerica/article/1574386/%E0%A6%AC%E0%A6%BF%E0%A6%B6%E0%A7%8D%E0%A6%AC%E0%A6%AC%E0%A7%8D%E0%A6%AF%E0%A6%BE%E0%A6%82%E0%A6%95%E0%A7%87%E0%A6%B0-%E0%A6%B8%E0%A6%AE%E0%A7%8D%E0%A6%AD%E0%A6%BE%E0%A6%AC%E0%A7%8D%E0%A6%AF-%E0%A6%AA%E0%A7%8D%E0%A6%B0%E0%A6%BE%E0%A6%B0%E0%A7%8D%E0%A6%A5%E0%A7%80-%E0%A6%87%E0%A6%AD%E0%A6%BE%E0%A6%99%E0%A7%8D%E0%A6%95%E0%A6%BE-%E0%A6%9F%E0%A7%8D%E0%A6%B0%E0%A6%BE%E0%A6%AE%E0%A7%8D%E0%A6%AA"></a>
<div class=image>
<noscript id=ari-image-703661574386 data-ari="{&quot;path&quot;:&quot;media\/2019\/01\/13\/7f45e68c6271d5afa236a474e13579c5-5c3aeb680af37.jpg?jadewits_media_id=1409285&quot;,&quot;ratio&quot;:[16,9],&quot;alt&quot;:&quot;\u09ac\u09bf\u09b6\u09cd\u09ac\u09ac\u09cd\u09af\u09be\u0982\u0995\u09c7\u09b0 \u09b8\u09ae\u09cd\u09ad\u09be\u09ac\u09cd\u09af \u09aa\u09cd\u09b0\u09c7\u09b8\u09bf\u09a1\u09c7\u09a8\u09cd\u099f \u09aa\u09cd\u09b0\u09be\u09b0\u09cd\u09a5\u09c0 \u0987\u09ad\u09be\u0999\u09cd\u0995\u09be \u099f\u09cd\u09b0\u09be\u09ae\u09cd\u09aa!&quot;}">
<img src="//paloimages.prothom-alo.com/contents/cache/images/400x225x1/uploads/media/2019/01/13/7f45e68c6271d5afa236a474e13579c5-5c3aeb680af37.jpg?jadewits_media_id=1409285" alt="বিশ্বব্যাংকের সম্ভাব্য প্রেসিডেন্ট প্রার্থী ইভাঙ্কা ট্রাম্প!"/>
</noscript>
<script data-id=ari-image-703661574386>
								jwARI.fetch( $( '#ari-image-703661574386' ) );
							</script>
<span class=content_type></span>
</div>
<div class="info has_ai">
<h2 class=title_holder>
<span class=title>বিশ্বব্যাংকের সম্ভাব্য প্রেসিডেন্ট প্রার্থী ইভাঙ্কা ট্রাম্প!</span>
</h2>
<div class=summery>
বিশ্বব্যাংকের প্রেসিডেন্ট পদে সম্ভাব্য প্রার্থীর তালিকায় যুক্তরাষ্ট্রের...
</div>
<div class=additional>
<a class="category aitm" href="/northamerica">উত্তর আমেরিকা</a>
</div>
</div>
</div>
</div></div>	</div>
</div></div></div></div></div></div><div id=wrapper_97371 class="wrapper    "><div class=inner><div id=div_97376 class="p_p     _col"><div class=inner><div id=widget_97381 class="widget_color_ widget_wrap"><div class="widget_text  widget">	<div class="widget_text_inner aunqur">
<div class=content><script>
$(document).ready(function(){	
	if($(".topic_list").is(':contains("নির্বাচনের তাজা খবর")')){ 
       
		$(".common_google_ads_top").css('display','none');
		$(".common_google_ads ").css('display','none');
		
		var d = new Date();
  		var hours24 = d.getHours();               
		
		if(hours24 %5 <= 1){			
	    /*==========Start Mens Fal ======= */
		$(".header_ad_block.advertisement").append('<a href="http://bit.ly/2RdJUFx" target="_blank"><img src="https://storage.googleapis.com/production-prothomalo/contents/uploads/media/2018/12/24/a5738f5d42be1a57d7d2afefa67ebee7-5c20ab7b4e08d.gif" alt="Rin" class="mobile_show"><img src="https://storage.googleapis.com/production-prothomalo/contents/uploads/media/2018/12/24/b99f74d27c753ec9ae82eda3d5432d46-5c20ac33c8abc.gif" alt="Rin" class="desktop_show"></a>');
		
		$(".Special_ad_r1").append('<a href="http://bit.ly/2EDX9JZ" target="_blank"><img src="https://storage.googleapis.com/production-prothomalo/contents/uploads/media/2018/12/26/2f8d04429b3751c7f8ee926b2782e35b-5c231516f39ad.gif" alt="Vaseline" class="mobile_show"><img src="https://storage.googleapis.com/production-prothomalo/contents/uploads/media/2018/12/26/76143bbd73a5aae009634521c4147433-5c2315423a25d.gif" alt="Vaseline" class="desktop_show"></a>');
		
		$(".Special_ad_r2").append('<a href="http://bit.ly/2Cm85t9" target="_blank"><img src="https://storage.googleapis.com/production-prothomalo/contents/uploads/media/2018/12/20/4737b599d8ec00ae2af8e7699ec7409c-5c1b8df1e5974.gif" alt="Pureit" class="mobile_show"><img src="https://storage.googleapis.com/production-prothomalo/contents/uploads/media/2018/12/20/c2e735b84dd0c70e5df9ec6a42d50778-5c1b8e2fba78c.gif" alt="Pureit" class="desktop_show"></a>');
		
		
		$(".Special_ad_b2").append('<a href="http://bit.ly/2GEc8FI" target="_blank"><img src="https://storage.googleapis.com/production-prothomalo/contents/uploads/media/2018/12/20/6c4e02fdc56b48a424b3159e6edfb072-5c1b870ac013a.gif" alt="mens fair & lovely" class="mobile_show"><img src="https://storage.googleapis.com/production-prothomalo/contents/uploads/media/2018/12/20/17bf9c84c05c8f1d079b837ac033c3d7-5c1b8768e8bb6.gif" alt="mens fair & lovely" class="desktop_show"></a>');



/*========== End Mens Fal ======= */
		}
		
		
		
		
		if(hours24 %5 == 2){
			
			/*==========Start Pureit ======= */			
			
		$(".header_ad_block.advertisement").append('<a href="http://bit.ly/2RdJUFx" target="_blank"><img src="https://storage.googleapis.com/production-prothomalo/contents/uploads/media/2018/12/24/a5738f5d42be1a57d7d2afefa67ebee7-5c20ab7b4e08d.gif" alt="Rin" class="mobile_show"><img src="https://storage.googleapis.com/production-prothomalo/contents/uploads/media/2018/12/24/b99f74d27c753ec9ae82eda3d5432d46-5c20ac33c8abc.gif" alt="Rin" class="desktop_show"></a>');
		
		$(".Special_ad_r1").append('<a href="http://bit.ly/2GEc8FI" target="_blank"><img src="https://storage.googleapis.com/production-prothomalo/contents/uploads/media/2018/12/20/2fcfe3e96aec9dc3dd65cc9e66c5e8b3-5c1b87c50b053.gif" alt="mens fair & lovely" class="mobile_show"><img src="https://storage.googleapis.com/production-prothomalo/contents/uploads/media/2018/12/20/b4b1b24e7dd6e78384c02086463ae01d-5c1b87df577b4.gif" alt="mens fair & lovely" class="desktop_show"></a>');
		
		$(".Special_ad_r2").append('<a href="http://bit.ly/2RdJUFx" target="_blank"><img src="https://storage.googleapis.com/production-prothomalo/contents/uploads/media/2018/12/24/99e9e05dec07751f7583dbe701f1a82d-5c20acbd6b010.gif" alt="Rin" class="mobile_show"><img src="https://storage.googleapis.com/production-prothomalo/contents/uploads/media/2018/12/24/e46258016554e2991ee57d2ea1433030-5c20acf0b1f8d.gif" alt="Rin" class="desktop_show"></a>');

$(".Special_ad_b2").append('<a href="http://bit.ly/2Cm85t9" target="_blank"><img src="https://storage.googleapis.com/production-prothomalo/contents/uploads/media/2018/12/20/03506b94ca7374e9d18cc2be314524e7-5c1b8d7c0508d.gif" alt="Pureit" class="mobile_show"><img src="https://storage.googleapis.com/production-prothomalo/contents/uploads/media/2018/12/20/afc22f05af8a151fa1c5007fc933c1ba-5c1b8da4005a4.gif" alt="Pureit" class="desktop_show"></a>');

/*==========End PureIt ======= */
		}
		
		if(hours24 %5 == 3){
			
			/*==========Start Rin ======= */			
			
		$(".header_ad_block.advertisement").append('<a href="http://bit.ly/2RdJUFx" target="_blank"><img src="https://storage.googleapis.com/production-prothomalo/contents/uploads/media/2018/12/24/a5738f5d42be1a57d7d2afefa67ebee7-5c20ab7b4e08d.gif" alt="Rin" class="mobile_show"><img src="https://storage.googleapis.com/production-prothomalo/contents/uploads/media/2018/12/24/b99f74d27c753ec9ae82eda3d5432d46-5c20ac33c8abc.gif" alt="Rin" class="desktop_show"></a>');

		$(".Special_ad_r1").append('<a href="http://bit.ly/2Cm85t9" target="_blank"><img src="https://storage.googleapis.com/production-prothomalo/contents/uploads/media/2018/12/20/4737b599d8ec00ae2af8e7699ec7409c-5c1b8df1e5974.gif" alt="Pureit" class="mobile_show"><img src="https://storage.googleapis.com/production-prothomalo/contents/uploads/media/2018/12/20/c2e735b84dd0c70e5df9ec6a42d50778-5c1b8e2fba78c.gif" alt="Pureit" class="desktop_show"></a>');
		
		$(".Special_ad_r2").append('<a href="http://bit.ly/2EDX9JZ" target="_blank"><img src="https://storage.googleapis.com/production-prothomalo/contents/uploads/media/2018/12/26/2f8d04429b3751c7f8ee926b2782e35b-5c231516f39ad.gif" alt="Vaseline" class="mobile_show"><img src="https://storage.googleapis.com/production-prothomalo/contents/uploads/media/2018/12/26/76143bbd73a5aae009634521c4147433-5c2315423a25d.gif" alt="Vaseline" class="desktop_show"></a>');
		
		$(".Special_ad_b2").append('<a href="http://bit.ly/2GEc8FI" target="_blank"><img src="https://storage.googleapis.com/production-prothomalo/contents/uploads/media/2018/12/20/6c4e02fdc56b48a424b3159e6edfb072-5c1b870ac013a.gif" alt="mens fair & lovely" class="mobile_show"><img src="https://storage.googleapis.com/production-prothomalo/contents/uploads/media/2018/12/20/17bf9c84c05c8f1d079b837ac033c3d7-5c1b8768e8bb6.gif" alt="mens fair & lovely" class="desktop_show"></a>');



/*==========End Rin ======= */
		}
		
		if(hours24 %5 == 4){
			
			/*==========Start Vaseline ======= */			
			
		$(".header_ad_block.advertisement").append('<a href="http://bit.ly/2RdJUFx" target="_blank"><img src="https://storage.googleapis.com/production-prothomalo/contents/uploads/media/2018/12/24/a5738f5d42be1a57d7d2afefa67ebee7-5c20ab7b4e08d.gif" alt="Rin" class="mobile_show"><img src="https://storage.googleapis.com/production-prothomalo/contents/uploads/media/2018/12/24/b99f74d27c753ec9ae82eda3d5432d46-5c20ac33c8abc.gif" alt="Rin" class="desktop_show"></a>');
		
		$(".Special_ad_r1").append('<a href="http://bit.ly/2GEc8FI" target="_blank"><img src="https://storage.googleapis.com/production-prothomalo/contents/uploads/media/2018/12/20/2fcfe3e96aec9dc3dd65cc9e66c5e8b3-5c1b87c50b053.gif" alt="mens fair & lovely" class="mobile_show"><img src="https://storage.googleapis.com/production-prothomalo/contents/uploads/media/2018/12/20/b4b1b24e7dd6e78384c02086463ae01d-5c1b87df577b4.gif" alt="mens fair & lovely" class="desktop_show"></a>');
		
		$(".Special_ad_r2").append('<a href="http://bit.ly/2Cm85t9" target="_blank"><img src="https://storage.googleapis.com/production-prothomalo/contents/uploads/media/2018/12/20/4737b599d8ec00ae2af8e7699ec7409c-5c1b8df1e5974.gif" alt="Pureit" class="mobile_show"><img src="https://storage.googleapis.com/production-prothomalo/contents/uploads/media/2018/12/20/c2e735b84dd0c70e5df9ec6a42d50778-5c1b8e2fba78c.gif" alt="Pureit" class="desktop_show"></a>');

		

$(".Special_ad_b2").append('<a href="http://bit.ly/2RdJUFx" target="_blank"><img src="https://storage.googleapis.com/production-prothomalo/contents/uploads/media/2018/12/24/a5738f5d42be1a57d7d2afefa67ebee7-5c20ab7b4e08d.gif" alt="Rin" class="mobile_show"><img src="https://storage.googleapis.com/production-prothomalo/contents/uploads/media/2018/12/24/b99f74d27c753ec9ae82eda3d5432d46-5c20ac33c8abc.gif" alt="Rin" class="desktop_show"></a>');

/*==========End Vaseline ======= */
		}
		
	}
});
</script>
<script>
$(document).ready(function(){
$(".right_part div[itemprop='articleBody'] > p:nth-child(3)").prepend('<div class="news_inner_spcl_ad "><a href="https://epaper.prothomalo.com/loginuser.php?utm_source=PALO&utm_medium=In-Article_Banner_Clicks&utm_campaign=Dec-18_V3" target="_blank"><img src="https://paloimages.prothom-alo.com/contents/cache/images/300X250X1/uploads/media/2018/12/22/587f1018bf93142a67cae107838987a9-5c1e16df2f7ef.png" alt="Eprothom Alo"></a></div>');
	
});
</script></div>
</div>
</div></div></div></div></div></div></div></div></div>
</div>
<div class=foot-portion>
<div class=foot-top-container>
<div class=foot-top>
<div class="foot-logo oh">
<a href="/"><img src="//paloimages.prothom-alo.com/contents/themes/public/style/images/foot-logo.png" alt="প্রথম আলো"/></a>
</div>
<div class=mobile-app-container>
<span>মোবাইল অ্যাপস ডাউনলোড করুন</span>
<a rel=nofollow class=apple-aps-icon href="https://itunes.apple.com/us/app/prothom-alo/id548596669" target=_blank>&nbsp;</a>
<a rel=nofollow class=android-aps-icon href="https://play.google.com/store/apps/details?id=com.mcc.prothomalo" target=_blank>&nbsp;</a>
</div>
</div>
</div>
<div class=foot_wrap_bg style="
				
					">
<div class=foot-middle-container>
<div class="foot_big_menu big_menu">
<div class=big_menu_top>
<div class=all-menu>
<ul id=8><li class="menu_page_id_37 menu_color_"><a class="static " href="/home">প্রচ্ছদ</a></li><li class="menu_page_id_102 menu_color_"><a class="dynamic " href="/bangladesh">বাংলাদেশ</a></li><li class="menu_page_id_153 menu_color_"><a class="dynamic " href="/international">আন্তর্জাতিক</a></li><li class="menu_page_id_189 menu_color_"><a class="dynamic " href="/economy">অর্থনীতি</a></li><li class="menu_page_id_216 menu_color_"><a class="dynamic " href="/sports">খেলা</a></li><li class="menu_page_id_246 menu_color_"><a class="dynamic " href="/opinion">মতামত</a></li><li class="menu_page_id_390 menu_color_"><a class="dynamic " href="/entertainment">বিনোদন</a></li><li class="menu_page_id_474 menu_color_"><a class="static " href="/features">ফিচার</a></li><li class="menu_page_id_285 menu_color_"><a class="dynamic " href="/life-style">জীবনযাপন</a></li><li class="menu_page_id_324 menu_color_"><a class="dynamic " href="/technology">বিজ্ঞান ও প্রযুক্তি</a></li><li class="menu_page_id_496 menu_color_"><a class="dynamic " href="/roshalo">রস+আলো</a></li><li class="menu_page_id_493 menu_color_"><a class="dynamic " href="/pachmisheli">পাঁচমিশালি</a></li><li class="menu_page_id_438 menu_color_"><a class="dynamic " href="/we-are">আমরা</a></li><li class="menu_page_id_463 menu_color_"><a class="dynamic " href="/onnoalo">শিল্প ও সাহিত্য</a></li><li class="menu_page_id_363 menu_color_"><a class="dynamic " href="/education">শিক্ষা</a></li></ul> </div>
<script>
                                jw_menu_fixer('.footer_menu','navigation');
                            </script>
<div class=special_menu>
<ul>
<li><a class=image_menu_icon href="/photo">ছবি</a></li>
<li><a class=video_menu_icon href="/video">ভিডিও</a></li>
<li><a class=archive_menu_icon href="/archive">আর্কাইভ</a></li>
</ul>
</div>
</div>
<div class=big_menu_bottom>
<div class=bmenu_bottom_left>
<div class=bmenu_bottom_toplinks>
<ul id=6><li class="menu_page_id_540 menu_color_"><a class="static " href="/advertise" target=_blank>বিজ্ঞাপন</a></li><li class="menu_page_id_544 menu_color_"><a class="static " href="/circulation" target=_blank>সার্কুলেশন</a></li><li class="menu_page_id_820 menu_color_"><a class="static " href="/hajj" target=_blank>পবিত্র হজ</a></li><li class="menu_page_id_736 menu_color_"><a class="dynamic archive" href="/durporobash" target=_blank>দূর পরবাস</a></li><li class="menu_page_id_536 menu_color_"><a class="dynamic " href="/northamerica" target=_blank>উত্তর আমেরিকা</a></li></ul>	</div>
<script>
								jw_menu_fixer('.footer_menu','navigation');
							</script>
<div class=bmenu_bottom_imagelinks>
<ul>
<li><a href="https://www.prothomalo.com/22221" target=_blank><span><img src="https://paloimages.prothom-alo.com/contents/themes/public/style/images/2221_icon.png" alt=""/></span>২২২২১</a></li>
<li><a href="https://www.prothomalo.com/trust" target=_blank><span><img src="https://paloimages.prothom-alo.com/contents/themes/public/style/images/trust_icon.png" alt=""/></span>ট্রাস্ট</a></li>
<li><a href="https://www.prothomalo.com/protichinta" target=_blank><span><img src="https://paloimages.prothom-alo.com/contents/themes/public/style/images/pchinta_icon.png" alt=""/></span>প্রতিচিন্তা</a></li>
<li><a href="https://www.prothomalo.com/kishoralo" target=_blank><span><img src="https://paloimages.prothom-alo.com/contents/cache/images/32X27X1/uploads/media/2018/09/24/e483aba8dfa8077ce2cb0b8e2429cc63-5ba8829143ed0.png" alt="কিশোর আলো"/></span>কিশোর আলো</a></li>
<li><a href="https://bit.ly/1yJDU9O" target=_blank rel=nofollow><span><img src="https://paloimages.prothom-alo.com/contents/themes/public/style/images/abcradio_icon.png" alt=""/></span>abc রেডিও</a></li>
<li><a href="https://www.prothomalo.com/bondhushava" target=_blank><span><img src="https://paloimages.prothom-alo.com/contents/cache/images/87x32x1/cache/uploads/media/2018/08/14/331e6cfb410b31c8288e18745ac83e24-5b72068060ea9.png" alt=""/></span></a></li>
</ul>	</div>
</div>
<div class=bmenu_bottom_right>
<p>
<em><strong>Prothom Alo</strong></em> is the highest circulated and most read newspaper in Bangladesh. The online portal of <em><strong>Prothom Alo</strong></em> is the most visited Bangladeshi and Bengali website in the world.
<br/> <a class=palo_privacy_link href="https://prothomalo.com/privacy" target=_blank title="Privacy Policy">Privacy Policy</a> | <a class=palo_privacy_link href="https://prothomalo.com/terms" target=_blank title="Terms of Use">Terms of Use</a>	</p>
</div>
</div>
</div>
</div>
<div class=foot-bottom-container>
<div class=foot-bottom>
&copy;&nbsp;স্বত্ব <span itemprop=publisher itemscope="" itemtype="http://schema.org/Organization"><span itemprop=name>প্রথম আলো</span> ১৯৯৮ - ২০১৯	</span> <div class=editor_publisher>সম্পাদক ও প্রকাশক: মতিউর রহমান</div>
<div class=office_address>প্রগতি ইনস্যুরেন্স ভবন, <span class=palo_break></span> ২০-২১ কারওয়ান বাজার , ঢাকা ১২১৫ </div>
<div class=offcie_contact>ফোন: ৮১৮০০৭৮-৮১, ফ্যাক্স: ৯১৩০৪৯৬,
<span class=palo_break></span>ইমেইল: <span class=palo_web_eng>info@prothomalo.com</span></div> </div>
</div>
</div>
</div>
</div>
<span class=back_to_top></span>
<script>
			$(window).scroll(function(){
				if($(this).scrollTop()>100){
					$('.back_to_top').fadeIn();
					}
				else{
					$('.back_to_top').fadeOut();
					}
				});
			$('.back_to_top').click(function(){
				$('body,html').animate({scrollTop:0},800);
				})
		</script>
<script>//$('body .content').disableSelection();</script>
<script>
if(url_dfp.search("/bangladesh-cricket-series") != -1){
document.write("<div id='div-gpt-ad-1499318314988-8'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-1499318314988-8'); });" + "</"+"scr"+"ipt>"+"</div>");
}
else if (url_dfp.search("/bangladesh") != -1 || url_dfp.search("/international") != -1 || url_dfp.search("/opinion") != -1 || url_dfp.search("/durporobash") != -1  || url_dfp.search("/pachmisheli") != -1  || url_dfp.search("/election") != -1 || url_dfp.search("/topic") != -1 || url_dfp.search("/photo") != -1 || url_dfp.search("/specialsupplement") != -1|| url_dfp.search("/cartoon") != -1 || url_dfp.search("/video") != -1 ) {
	document.write("<div id='div-gpt-ad-1499318314988-6'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-1499318314988-6'); });" + "</"+"scr"+"ipt>"+"</div>");
	}
	// Fixture page Landing
else if(url_dfp.search("/sports-fixture") != -1){

}
else if (url_dfp.search("/sports") != -1 ) {
	document.write("<div id='div-gpt-ad-1499318314988-8'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-1499318314988-8'); });" + "</"+"scr"+"ipt>"+"</div>");
}
/*else if (url_dfp.search("/sports-results") != -1 ) {
	document.write("<div id='div-gpt-ad-1499318314988-8'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-1499318314988-8'); });" + "</"+"scr"+"ipt>"+"</div>");
} */
else if (url_dfp.search("/fifa-world-cup") != -1 ) {
	document.write("<div id='div-gpt-ad-1499318314988-8'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-1499318314988-8'); });" + "</"+"scr"+"ipt>"+"</div>");
}

else if(url_dfp.search("/entertainment") != -1 || url_dfp.search("/alapon") != -1 || url_dfp.search("/music") != -1 || url_dfp.search("/dance") != -1 || url_dfp.search("/somalochona") != -1 || url_dfp.search("/tarokader-lekha") != -1){
	document.write("<div id='div-gpt-ad-1499318314988-2'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-1499318314988-2'); });" + "</"+"scr"+"ipt>"+"</div>");
}
else if (url_dfp.search("/lifestyle") != -1 || url_dfp.search("/we-are-") != -1 || url_dfp.search("/female-stage") != -1 || url_dfp.search("/personality") != -1 || url_dfp.search("/torun") != -1 || url_dfp.search("/international-womens-day") != -1 || url_dfp.search("/art-and-literature-") != -1 || url_dfp.search("/poem") != -1 || url_dfp.search("/short-stories") != -1 || url_dfp.search("/industrial-art") != -1 || url_dfp.search("/meeting") != -1 || url_dfp.search("/treatise") != -1 || url_dfp.search("/translation") != -1 || url_dfp.search("/children-s-literature") != -1 || url_dfp.search("/book-discussion") != -1 || url_dfp.search("/child") != -1 || url_dfp.search("/kishor") != -1 || url_dfp.search("/personality") != -1 || url_dfp.search("/torun") != -1 || url_dfp.search("/probashi") != -1) {
	document.write("<div id='div-gpt-ad-1499318314988-4'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-1499318314988-4'); });" + "</"+"scr"+"ipt>"+"</div>");
}
else if (url_dfp.search("/technology") != -1) {	
	document.write("<div id='div-gpt-ad-1499318314988-9'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-1499318314988-9'); });" + "</"+"scr"+"ipt>"+"</div>");
}

else if (url_dfp.search("/economy") != -1 || url_dfp.search("/budget") != -1) {
	document.write("<div id='div-gpt-ad-1499318314988-0'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-1499318314988-0'); });" + "</"+"scr"+"ipt>"+"</div>");
}

else if (url_dfp.search("/northamerica") != -1 || url_dfp.search("/canada") != -1  || url_dfp.search("/america") != -1) {
	document.write("<div id='div-gpt-ad-1499318314988-7'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-1499318314988-7'); });" + "</"+"scr"+"ipt>"+"</div>");
}

else if (url_dfp.search("/education") != -1 || url_dfp.search("/institution") != -1 || url_dfp.search("/meritorious") != -1 || url_dfp.search("/preparation") != -1 || url_dfp.search("/jenerakhun") != -1 || (url_dfp.search("-education") != -1 && url_dfp.search("opinion-education") == -1)) {
	document.write("<div id='div-gpt-ad-1499318314988-1'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-1499318314988-1'); });" + "</"+"scr"+"ipt>"+"</div>");
}
else if (url_dfp.search("/naksha") != -1 || url_dfp.search("/shapno") != -1 || url_dfp.search("/adhuna") != -1 || url_dfp.search("/holiday") != -1 || url_dfp.search("roshalo") != -1 ||url_dfp.search("/ananda") != -1 ) {	
	document.write("<div id='div-gpt-ad-1499318314988-5'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-1499318314988-5'); });" + "</"+"scr"+"ipt>"+"</div>");
}
else if (url_dfp.search("/features") != -1 || url_dfp.search("/sabar-age-shisu") != -1 || url_dfp.search("/gollachut") != -1 ||
url_dfp.search("/anna-alo") != -1 || url_dfp.search("/shilpo-o-sahitto") != -1 || url_dfp.search("/alokito-chittagong") != -1 ||
url_dfp.search("/amader-kotha-shono") != -1 || url_dfp.search("/projonmo-dot-com") != -1 || url_dfp.search("/choltibishow") != -1) {
	
	document.write("<div id='div-gpt-ad-1499318314988-3'><" + "scr" + "ipt>" + "googletag.cmd.push(function() { googletag.display('div-gpt-ad-1499318314988-3'); });" + "</"+"scr"+"ipt>"+"</div>");
}else if(url_dfp.search("/sruti") != -1){

}
</script>
<style>
.anchor_ad_wrapper{position:fixed;bottom:-92px;height:72px;left:0;right:0;padding:20px 0 0;z-index:9}
#anchor_ad_close{width:22px;height:16px;border-radius:28px 28px 0 0;background-color:#D8D8D8;margin:0 auto;padding:8px 10px}
#anchor_ad_close div{background:grey;width:100%;height:2px;margin:2px 0}
.anchor_ad_close_wrapper{position:absolute;left:0;right:0;top:0;height:32px}
.anchor_ad_top_border{background:#D8D8D8;position:absolute;top:20px;left:0;right:0;height:12px;box-shadow:0 0 8px #999}
.anchor_ad_container{background-color:#000;width:100%;height:60px;position:absolute;bottom:0}
</style>
<div class=anchor_ad_wrapper>
<div class=anchor_ad_top_border></div>
<div class=anchor_ad_close_wrapper>
<div id=anchor_ad_close>
<div></div>
<div></div>
<div></div>
</div>
</div>
<div class=anchor_ad_container>
<div id=div-gpt-ad-1465904547187-112>
<script>
			if(detectmob()){
				googletag.cmd.push(function() {
					if (isHomepage()){
						googletag.pubads().display('/85406138/Mobile_HP_Anchor', [[360, 60], [320, 50]], 'div-gpt-ad-1465904547187-112');
					}else{
						googletag.pubads().display('/85406138/Mobile_Article_Anchor', [[360, 60], [320, 50]], 'div-gpt-ad-1465904547187-112');
					}
				});
			}
			</script>
</div>
</div>
</div>
<script>

var flag = true;
var isMobile = detectmob();
$(window).scroll(function(){
	if(isMobile && flag){
		if($(this).scrollTop() > 60){
			flag = false;
			$('.back_to_top').css('bottom', 82);
			$('.foot-portion').css('margin-bottom',72);
			$('.anchor_ad_wrapper').animate({
				bottom:0	
			},500);
		}
	}
});

$(document).ready(function(e) {
    $('#anchor_ad_close').click(function(){
		$('.back_to_top').css('bottom', 20);
		$('.foot-portion').css('margin-bottom',0);
		$('.anchor_ad_wrapper').hide();
	});
});
</script>
<style>
/*.site_logo{
	margin-top:3px !important;
}
@media only screen and (max-width: 800px){
.site_logo img {
    height: 46px !important;
}
}*/
</style>
<script>
//$(".site_logo a img").fadeOut("slow");
/*
$(".site_logo a img").attr("src","https://storage.googleapis.com/production-prothomalo/contents/uploads/media/2018/12/15/17aa9a7993d58a11e025675836b89985-5c1511005bbed.png");
$(".site_logo a img").fadeIn("slow");
//$(".site_logo a img").attr("height","46");
*/
</script>
<script>
if (url_dfp.search("/international") != -1) {
	
	$( ".secondary_header" ).css({
	"background-image": "URL('https://storage.googleapis.com/production-prothomalo/contents/uploads/default/2017/01/28/7892d7bf26c46e1c0f59162c60cdbab3-588c78893db67.png')"
});

}

if (url_dfp.search("/sports") != -1) {
$( ".secondary_header" ).css({
	"background-image": "URL('https://storage.googleapis.com/production-prothomalo/contents/uploads/default/2017/01/28/0220b43742d316d91b2b1b4af72fa7a1-588c5702a388e.png')"
});
}

if (url_dfp.search("/entertainment") != -1 || url_dfp.search("/alapon") != -1 || url_dfp.search("/music") != -1) {
$( ".secondary_header" ).css({
	"background-image": "URL('https://storage.googleapis.com/production-prothomalo/contents/uploads/default/2017/01/28/c73f77d365ff874572e87e5e41423c08-588c66c1bcbed.png')"
});
}

if (url_dfp.search("/economy") != -1) {
$( ".secondary_header" ).css({
	"background-image": "URL('https://storage.googleapis.com/production-prothomalo/contents/uploads/default/2017/01/29/5aa76a8bafceff8c54822a4471233f2c-588da3ee698a5.png')"
});
}
if (url_dfp.search("/bangladesh") != -1) {
$( ".secondary_header" ).css({
	"background-image": "URL('https://storage.googleapis.com/production-prothomalo/contents/uploads/default/2017/01/22/27ab23e0abfef085995032b4037b236e-58843f438f52d.png')"
});
}
if (url_dfp.search("/life-style") != -1 || url_dfp.search("/lifestyle") != -1) {
$( ".secondary_header" ).css({
	"background-image": "URL('https://storage.googleapis.com/production-prothomalo/contents/uploads/default/2017/01/28/e215d9a4d4ca9641c888ca8ac2eca1ba-588c57fe99228.png')"
});
}
if (url_dfp.search("/video") != -1 ) {
$( ".secondary_header" ).css({
	"background-image": "URL('https://storage.googleapis.com/production-prothomalo/contents/uploads/default/2017/04/18/a7a62a3f16403d9fd9c3878ea001ae22-58f5ec2b034b8.png')"
});
}
if (url_dfp.search("/northamerica") != -1 || url_dfp.search("/canada") != -1 || url_dfp.search("/america") != -1) {
$( ".secondary_header" ).css({
	"background-image": "URL('https://storage.googleapis.com/production-prothomalo/contents/uploads/default/2017/03/23/1f95edb6f210cdecb24d97aae33131b6-58d381de1d307.png')"
});
}

</script>
<script>
$('.contents_tabbed .view_all_wrap .view_all').html('আরও');
</script>
<script>
var datalayer= {
z_cltr: '%%CLICK_URL_UNESC%%',
z_imtr: '%%VIEW_URL_UNESC%%'
}
</script>
<div id=zcf330014-c347-407c-8135-b89c82d1eef1 style=display:none></div>
<script>!function(a,n,e,t,r){tagsync=e;var c=window[a];if(tagsync){var d=document.createElement("script");d.src="https://3407.tm.zedo.com/v1/f0a39a86-3b12-40be-863f-e055c8a5924a/atm.js",d.async=!0;var i=document.getElementById(n);if(null==i||"undefined"==i)return;i.parentNode.appendChild(d,i),d.onload=d.onreadystatechange=function(){var a=new zTagManager(n);a.initTagManager(n,c,this.aync,t,r)}}else document.write("<script src='https://3407.tm.zedo.com/v1/f0a39a86-3b12-40be-863f-e055c8a5924a/tm.js?data="+a+"'><"+"/script>")}("datalayer","zcf330014-c347-407c-8135-b89c82d1eef1",true, 0 , 0);
</script>
</body>
</html>
"""
	# html_string
	article.download(html_string)
	article.parse()
	item = dict()
	item['url'] = article.url
	item['title'] = article.title
	item['published_date'] = article.publish_date.strftime('%Y/%m/%d')
	item['text'] = article.text
	# item['html'] = htmlmin.minify(article.html, remove_empty_space=True)
	item['movies'] = list(article.movies)
	item['source_url'] = article.source_url
	if(len(article.tags) > 0):
		item['tags'] = list(article.tags)
	item['summary'] = article.summary
	item['top_image'] = article.top_image
	item['images'] = list(article.images)
	item['keywords'] = list(article.keywords)
	return flask.jsonify(item)
app.config['JSON_AS_ASCII'] = False
app.run(host='0.0.0.0')