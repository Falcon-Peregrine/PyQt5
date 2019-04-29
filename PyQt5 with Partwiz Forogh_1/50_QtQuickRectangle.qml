import QtQuick.Window 2.2
import QtQuick 2.3

Window {
visible:true
width:600 
height:400
color:"red"
title:"My Simple Window"

Rectangle {
	id:blueRect
	width:200
	height:64
	color:"blue"
	anchors.centerIn:parent
	border.color:"black"
	border.width:7
	radius:20
	opacity:.50

	

}


Text {
	id:text1
	text:"Hello Application"
	font.pixelSize:40
	font.bold:true
	color:"white"
	anchors.centerIn:parent
	

}




}