$(function() {
    var txt = "";
    //blockquote
    function makeblock() {
        var a = txt;
        for (var i = 0; i < 100; i++) {
            a = a.replace(/(^\>+)((.*\n\>)*.*)/gm, "$1<blockquote><p>$2</p></blockquote>");
            var lin = a.split("\n");
            var il = 0;
            for (var j = 0; j < lin.length; j++) {
                if (lin[j].startsWith(">")) {
                    lin[j] = lin[j].substr(1);
                    il++;
                }
            }
            a = lin.join("\n");
        }
        txt = a;
    };

    //ol i li
    function makeli() {
        var lin = txt.replace(/\r/g, "").split("\n");
        var n = 1;
        for (var i = 0; i < lin.length; i++) {
            var x = lin[i];
            if (x.startsWith(n + ".")) {
                lin[i] = "<li>" + lin[i].replace(/^\d+.? */g, "").replace(/\r/g, "") + "</li>";
                if (n == 1) {
                    lin[i] = "<ol>" + lin[i];
                }
                n++;
            } else {
                if (n != 1) {
                    lin[i-1] = lin[i-1] + "</ol>";
                }
                n = 1;
            }
        }
        txt = lin.join("\r\n");
    };

    //p
    function makep() {
        var lin = txt.replace(/\r/g, "").split("\n");
        for (var i = 0; i < lin.length; i++) {
            var x = lin[i].replace(/\r\n/gm, "");
            if ((!x.startsWith("<") && !x.endsWith(">") && x != "")) {
                lin[i] = "<p>" + lin[i] + "</p>";
            }
        }
        txt = lin.join("\r\n");
    }

    //reszta
    function rest(){
        var lin = txt.replace(/\r/g, "").split("\n");
        for (var i = 0; i < lin.length; i++) {
            lin[i] = lin[i].replace(/(?:^|([A-Za-z ]))(\_)(.*?)\_/gm, "$1<sub>$3</sub>");
            lin[i] = lin[i].replace(/(?:^|([A-Za-z ]))(\^)(.*?)\^/gm, "$1<sup>$3</sup>");
            lin[i] = lin[i].replace(/(?:^|( ))([\"\'])(.*?)\2/gm, "$1<q>$3</q>");
            lin[i] = lin[i].replace(/(^\r\n)+$/gm, ""); 
        }
        txt = lin.join("\r\n");
    }

    //main
    function final() {
        txt = taketext.value;
        makeblock();
        makeli();
        makep();
        rest();
        givescript.value = txt;
    };

    $("#taketext").on({
        input: final
    });
    final();
});