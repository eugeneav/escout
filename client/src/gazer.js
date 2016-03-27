
(function() {

	String.prototype.escout_hash = function() {  		
  		var hash = 0, i, chr, len;
  		
  		if (this.length == 0) 
  			return hash;
  		
  		for (i = 0, len = this.length; i < len; i++) {
    		chr   = this.charCodeAt(i);
    		hash  = ((hash << 5) - hash) + chr;
    		hash |= 0; // Convert to 32bit integer
  		}

  		return hash * -1;
	};

	function randomString(length, chars) {
    	var mask = '';
    	if (chars.indexOf('a') > -1) mask += 'abcdefghijklmnopqrstuvwxyz';
    	if (chars.indexOf('A') > -1) mask += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    	if (chars.indexOf('#') > -1) mask += '0123456789';
   		if (chars.indexOf('!') > -1) mask += '~`!@#$%^&*()_+-={}[]:";\'<>?,./|\\';
    	var result = '';
    	for (var i = length; i > 0; --i) result += mask[Math.round(Math.random() * (mask.length - 1))];
    	return result;
	}


	function Cookie() {};
  
  Cookie.prototype.get = function (sKey) {
    if (!sKey) { 
    	return null; 
    }
    return decodeURIComponent(document.cookie.replace(new RegExp("(?:(?:^|.*;)\\s*" + encodeURIComponent(sKey).replace(/[\-\.\+\*]/g, "\\$&") + "\\s*\\=\\s*([^;]*).*$)|^.*$"), "$1")) || null;
  };

  Cookie.prototype.set = function (sKey, sValue, vEnd, sPath, sDomain, bSecure) {
    
    if (!sKey || /^(?:expires|max\-age|path|domain|secure)$/i.test(sKey)) { 
    	return false; 
    }

    var sExpires = "";

    if (vEnd) {
      switch (vEnd.constructor) {
        case Number:
          sExpires = vEnd === Infinity ? "; expires=Fri, 31 Dec 9999 23:59:59 GMT" : "; max-age=" + vEnd;
          break;
        case String:
          sExpires = "; expires=" + vEnd;
          break;
        case Date:
          sExpires = "; expires=" + vEnd.toUTCString();
          break;
      }
    }

    document.cookie = encodeURIComponent(sKey) + "=" + encodeURIComponent(sValue) + sExpires + (sDomain ? "; domain=" + sDomain : "") + (sPath ? "; path=" + sPath : "") + (bSecure ? "; secure" : "");
    return true;
  };

  Cookie.prototype.remove = function (sKey, sPath, sDomain) {
    if (!this.hasItem(sKey)) {
     return false; 
    }
    document.cookie = encodeURIComponent(sKey) + "=; expires=Thu, 01 Jan 1970 00:00:00 GMT" + (sDomain ? "; domain=" + sDomain : "") + (sPath ? "; path=" + sPath : "");
    return true;
  };

  Cookie.prototype.has = function (sKey) {
    if (!sKey) { return false; }
    return (new RegExp("(?:^|;\\s*)" + encodeURIComponent(sKey).replace(/[\-\.\+\*]/g, "\\$&") + "\\s*\\=")).test(document.cookie);
  };

  Cookie.prototype.getKeys = function () {
    var aKeys = document.cookie.replace(/((?:^|\s*;)[^\=]+)(?=;|$)|^\s*|\s*(?:\=[^;]*)?(?:\1|$)/g, "").split(/\s*(?:\=[^;]*)?;\s*/);
    for (var nLen = aKeys.length, nIdx = 0; nIdx < nLen; nIdx++) { aKeys[nIdx] = decodeURIComponent(aKeys[nIdx]); }
    return aKeys;
  };

	function RemoteTracker() {
		
		var oClient          = window.escout_client[0]();
		var oCookie          = new Cookie();

		this.clientId        = oClient.identifier;
		this.clientHost      = window.location.hostname;

		if(oCookie.has('escout_session_id')) {
			this.clientSessionId = oCookie.get('escout_session_id');
		} else {
			var clientSessionId = randomString(64,"#Aa");
			//var clientSessionId = this.clientHost + this.clientId + new Date().getTime();
			this.clientSessionId = clientSessionId;
			oCookie.set('escout_session_id', this.clientSessionId);
		}
	}

	RemoteTracker.prototype.clientId        = null;
	RemoteTracker.prototype.clientHost      = null;
	RemoteTracker.prototype.clientSessionId = null;

	RemoteTracker.prototype.send = function(data) {
		var img = new Image();
		img.src = "http://127.0.0.1:8000/gazer/_tf.gif?tm=" + new Date().getTime() + "&ci=" + encodeURIComponent(this.clientId) + "&ch=" + encodeURIComponent(this.clientHost)
		//img.src = "//escout.loc/gazer/_tf.gif?tm=" + new Date().getTime() + "&ci=" + encodeURIComponent(this.clientId) + "&ch=" + encodeURIComponent(this.clientHost)
		 + "&csi=" + encodeURIComponent(this.clientSessionId) + "&d=" + encodeURIComponent(data);  
	};

	function Log(oRemoteTracker) {
		this.remoteTracker = oRemoteTracker;
	}

	Log.prototype.remoteTracker = null
	Log.prototype.error = function(code, message, stacktrace) {
		
		var data = {
			code: code,
			message: message,
			stacktrace: stacktrace
		};

		this.remoteTracker.send(JSON.stringify(data));
	}

	function Event(oRemoteTracker) {
		this.remoteTracker = oRemoteTracker;
	}

	Event.prototype.remoteTracker = null;
	Event.prototype.track = function(event, comment) {
		
		// Prepare data
		var data = {
			event: event,
			message: comment
		};

		this.remoteTracker.send(JSON.stringify(data));
	}

	function Escout() {
		this.log   = new Log(new RemoteTracker());
		this.event = new Event(new RemoteTracker());
	};

	Escout.prototype.log   = null;
	Escout.prototype.event = null;

	window.escout = new Escout();
	
})(window)