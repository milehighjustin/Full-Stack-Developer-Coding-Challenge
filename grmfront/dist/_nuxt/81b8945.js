(window.webpackJsonp=window.webpackJsonp||[]).push([[5],{257:function(t,o,e){"use strict";e.r(o);e(261),e(256),e(409);var l={name:"AppLayout",data:function(){return{logoutshow:!0}},head:function(){return{bodyAttrs:{class:"dark-theme"}}},methods:{switchlight:function(){var body=document.body;"dark-theme"==body.classList?(body.classList.remove("dark-theme"),body.classList.toggle("light-theme"),body.style.backgroundColor="white"):(body.classList.remove("light-theme"),body.classList.toggle("dark-theme"),body.style.backgroundColor="#101923")},logout:function(){window.localStorage.clear(),window.location.href="./"}},mounted:function(){window.localStorage.getItem("authtoken")||(this.logoutshow=!1)}},c=e(52),component=Object(c.a)(l,(function(){var t=this,o=t.$createElement,e=t._self._c||o;return e("div",[e("rux-global-status-bar",[e("h1",{staticStyle:{color:"white"}},[e("rux-icon",{attrs:{color:"#fff",icon:"satellite-transmit"}}),t._v(" GRM Dashboard")],1),e("rux-clock"),e("div",{on:{click:t.switchlight}},[e("h1",{staticStyle:{color:"white"}},[e("b-icon-square-half")],1)]),t.logoutshow?e("div",{on:{click:t.logout}},[e("h1",{staticStyle:{color:"white"}},[e("b-icon-door-open")],1)]):t._e()],1),t._v(" "),t._t("default")],2)}),[],!1,null,null,null);o.default=component.exports}}]);