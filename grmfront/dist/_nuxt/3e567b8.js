(window.webpackJsonp=window.webpackJsonp||[]).push([[4],{262:function(t,e,r){"use strict";r.r(e);r(15),r(259),r(256);var n={name:"Dbcontent",data:function(){return{alerts:{},contact:{},user:{}}},head:function(){return{bodyAttrs:{class:"dark-theme"}}},methods:{processAppData:function(data){this.alerts=data.alerts,this.contacts=data.contacts,this.user=data.user},errorNotify:function(){}},mounted:function(){var t=this;try{var e={method:"POST",headers:{"Content-Type":"Application/json",authtoken:window.localStorage.getItem("authtoken")},body:JSON.stringify({status:"get"})};fetch("/getappdata",e).then((function(t){return t.json()})).then((function(data){return t.processAppData(data)})).catch((function(e){return t.errorNotify()}))}catch(t){this.errorNotify()}}},o=r(51),component=Object(o.a)(n,(function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",[r("b-container",{attrs:{fluid:""}},[r("b-row",[r("b-col",{attrs:{cols:"5"}},[r("tr",[r("h1",[t._v("Alerts")])]),t._v(" "),r("table",{staticClass:"rux-table"},[r("tr",{staticClass:"rux-table__column-head"},[r("th",[t._v("Message")]),t._v(" "),r("th",[t._v("Category")]),t._v(" "),r("th",[t._v("Time")])]),t._v(" "),t._l(t.alerts,(function(e){return r("tr",{key:e},[r("td",[t._v(t._s(e.errorMessage))]),r("td",[t._v(t._s(e.errorCategory))]),r("td",[t._v(t._s(e.errorTime))])])}))],2)]),t._v(" "),r("b-col",{attrs:{cols:"7"}},[r("tr",[r("h1",[t._v("Contacts")])]),t._v(" "),r("table",{staticClass:"rux-table"},[r("tr",{staticClass:"rux-table__column-head"},[r("th",[t._v("Name")]),t._v(" "),r("th",[t._v("Status")]),t._v(" "),r("th",[t._v("Begin Timestamp")]),t._v(" "),r("th",[t._v("End Timestamp")])]),t._v(" "),t._l(t.contacts,(function(e){return r("tr",{key:e},[r("td",[t._v(t._s(e.contactName))]),r("td",[t._v(t._s(e.contactStatus))]),r("td",[t._v(t._s(e.contactBeginTimestamp))]),r("td",[t._v(t._s(e.contactEndTimestamp))])])}))],2)])],1)],1)],1)}),[],!1,null,"6cdd6479",null);e.default=component.exports}}]);