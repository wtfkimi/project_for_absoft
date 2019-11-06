# project_for_absoft
This is project for absoft
For people which are сheck my tests!
I don't used GMAIL API. It would be easier to use SMTP server. Cause one precepts of "Zen of Python" - it is "Simple is better than complex.". So I decided use SMTP server) 

I create my project using pattern Page Object Model and framework Pytest. If you don't know anything about this pattern, here you can read "https://habr.com/ru/post/145848/";
"https://medium.com/tech-tajawal/page-object-model-pom-design-pattern-f9588630800b"

First:
Install requirements.txt

Second:
Read conftest.py!

In framework pytest You can open my tests in Chrome browser and Firefox browser, using fixture "--browser_name=choose_browser(firefox or chrome)", but default
tests will starts in Firefox browser, which I recommend. Cause in Chrome browser tests are unstable. About fixtures you can read there "https://habr.com/ru/post/269759/" and 
there "http://doc.pytest.org/en/latest/example/markers.html"

Third:
In project you can use markers, which you can see in pytest.ini, more about markers you can see there "https://habr.com/ru/post/269759/"
