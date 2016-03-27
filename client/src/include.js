//<script> include me
    (function (window, document, id) {
        (window[id] = window[id] || []).push(
                function () {
                    /*try {

                         w.yaCounter28460466 = new Ya.Metrika({id: 28460466, webvisor: true});
                         add callback here
                    } catch (e) {
                    }*/

                    return {identifier: "ESA-999999999"};
                });

        var oNode = document.getElementsByTagName("script")[0],
            oScript = document.createElement("script"),
            scriptIncludingFunction = function () {
                oNode.parentNode.insertBefore(oScript, oNode);
            };
        
        oScript.type  = "text/javascript";
        oScript.async = true;
        oScript.src = (document.location.protocol == "https:" ? "https:" : "http:") + "//escout.loc/scripts/gazer.js";
        
        if (window.opera == "[object Opera]") {
            d.addEventListener("DOMContentLoaded", scriptIncludingFunction, false);
        } else {
            scriptIncludingFunction();
        }

    })(window, document, 'escout_client')
//</script>