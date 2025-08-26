var disqus_shortname = 'httpbbk0701githubiomysiteoutput';

var disqus_config = function () {
    var disqusThread = document.getElementById('disqus_thread');
    this.page.identifier = disqusThread.getAttribute('data-identifier');
};

(function() {
    var d = document, s = d.createElement('script');
    s.src = 'https://' + disqus_shortname + '.disqus.com/embed.js';
    s.setAttribute('data-timestamp', +new Date());
    (d.head || d.body).appendChild(s);
})();
