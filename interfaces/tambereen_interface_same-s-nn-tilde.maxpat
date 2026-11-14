{
	"patcher" : 	{
		"fileversion" : 1,
		"appversion" : 		{
			"major" : 8,
			"minor" : 5,
			"revision" : 8,
			"architecture" : "x64",
			"modernui" : 1
		}
,
		"classnamespace" : "box",
		"rect" : [ 153.0, 179.0, 1639.0, 916.0 ],
		"bglocked" : 0,
		"openinpresentation" : 1,
		"default_fontsize" : 12.0,
		"default_fontface" : 0,
		"default_fontname" : "Arial",
		"gridonopen" : 1,
		"gridsize" : [ 15.0, 15.0 ],
		"gridsnaponopen" : 1,
		"objectsnaponopen" : 1,
		"statusbarvisible" : 2,
		"toolbarvisible" : 0,
		"lefttoolbarpinned" : 0,
		"toptoolbarpinned" : 0,
		"righttoolbarpinned" : 0,
		"bottomtoolbarpinned" : 0,
		"toolbars_unpinned_last_save" : 0,
		"tallnewobj" : 0,
		"boxanimatetime" : 200,
		"enablehscroll" : 1,
		"enablevscroll" : 1,
		"devicewidth" : 0.0,
		"description" : "",
		"digest" : "",
		"tags" : "",
		"style" : "",
		"subpatcher_template" : "",
		"assistshowspatchername" : 0,
		"boxes" : [ 			{
				"box" : 				{
					"id" : "obj-61",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 179.0, 290.0, 41.0, 22.0 ],
					"text" : "/ack 1"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-58",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 179.0, 350.0, 138.0, 22.0 ],
					"text" : "udpsend 127.0.0.1 7005"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-26",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"patching_rect" : [ 152.0, 37.0, 56.0, 22.0 ],
					"text" : "route /on"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-43",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 1714.0, 57.0, 156.0, 22.0 ],
					"text" : "disconnect terrain mc 32 64"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-44",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 1696.0, 26.0, 143.0, 22.0 ],
					"text" : "connect mc decoder 0 64"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-48",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1696.0, 90.0, 145.0, 22.0 ],
					"text" : "v8 connection @embed 1"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-19",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"patching_rect" : [ 1085.0, 1.0, 58.0, 22.0 ],
					"text" : "loadbang"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-39",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 746.0, 366.0, 83.0, 22.0 ],
					"text" : "loadmess 100"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-73",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 1384.863520681858063, 177.0, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-67",
					"maxclass" : "newobj",
					"numinlets" : 5,
					"numoutlets" : 4,
					"outlettype" : [ "int", "", "", "int" ],
					"patching_rect" : [ 1233.0, 45.0, 61.0, 22.0 ],
					"text" : "counter 2"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-65",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 1162.0, 19.0, 58.0, 58.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 307.0, 47.0, 50.0, 50.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-60",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 5,
					"outlettype" : [ "", "", "", "", "" ],
					"patching_rect" : [ 1368.5, 297.0, 147.0, 22.0 ],
					"text" : "regexp \"text \" @substitute"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-10",
					"keymode" : 1,
					"linecount" : 4,
					"maxclass" : "textedit",
					"numinlets" : 1,
					"numoutlets" : 4,
					"outlettype" : [ "", "int", "", "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 1384.863520681858063, 218.401527047157288, 722.662773251533508, 25.598472952842712 ],
					"presentation" : 1,
					"presentation_linecount" : 4,
					"presentation_rect" : [ 687.75, 156.0, 657.932491302490234, 19.696967959403992 ],
					"text" : "1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-45",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 565.25, 460.0, 29.5, 22.0 ],
					"text" : "1."
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-6",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1277.5, 903.0, 231.0, 22.0 ],
					"saved_object_attributes" : 					{
						"allwindowsactive" : 0,
						"appicon_mac" : "",
						"appicon_win" : "",
						"audiosupport" : 1,
						"bundleidentifier" : "com.mycompany.myprogram",
						"cantclosetoplevelpatchers" : 0,
						"cefsupport" : 1,
						"copysupport" : 1,
						"database" : 0,
						"extensions" : 1,
						"gensupport" : 1,
						"midisupport" : 1,
						"noloadbangdefeating" : 0,
						"overdrive" : 0,
						"preffilename" : "",
						"searchformissingfiles" : 1,
						"statusvisible" : 1,
						"usesearchpath" : 0
					}
,
					"text" : "standalone @cantclosetoplevelpatchers 0"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-153",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "open" ],
					"patching_rect" : [ 1290.0, 533.5, 42.0, 22.0 ],
					"text" : "t open"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-124",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 1290.0, 489.5, 113.0, 22.0 ],
					"presentation" : 1,
					"presentation_linecount" : 2,
					"presentation_rect" : [ 411.0, 394.0, 92.0, 35.0 ],
					"style" : "default",
					"text" : "open audio settings"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-74",
					"ignoreclick" : 1,
					"maxclass" : "ezdac~",
					"numinlets" : 2,
					"numoutlets" : 0,
					"patching_rect" : [ 1290.0, 577.5, 45.0, 45.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 521.0, 393.0, 36.899999439716339, 36.899999439716339 ],
					"style" : "default"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-71",
					"items" : [ "All", "Dimensions", ",", "First", "Dimension", ",", "Custom" ],
					"maxclass" : "umenu",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "int", "", "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 1253.5, 77.0, 162.399982392787933, 22.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 267.200003981590271, 105.5, 123.200001835823059, 22.0 ],
					"textcolor" : [ 0.086274509803922, 0.713725490196078, 0.776470588235294, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontsize" : 20.0,
					"id" : "obj-57",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 691.0, 290.0, 114.0, 29.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 412.000006139278412, 82.0, 147.0, 29.0 ],
					"text" : "Novelified"
				}

			}
, 			{
				"box" : 				{
					"fontsize" : 20.0,
					"id" : "obj-56",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 468.0, 530.0, 224.0, 29.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 99.0, 244.200004100799561, 56.800000846385956, 29.0 ],
					"text" : "Mix"
				}

			}
, 			{
				"box" : 				{
					"fontsize" : 20.0,
					"id" : "obj-55",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 367.0, 215.0, 71.0, 29.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 98.0, 87.0, 135.0, 29.0 ],
					"text" : "RAW"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-51",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "multichannelsignal" ],
					"patching_rect" : [ 722.0, 512.0, 50.0, 22.0 ],
					"text" : "mc.list~"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-29",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 968.0, 33.5, 70.0, 22.0 ],
					"text" : "loadmess 0"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-53",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "bang", "" ],
					"patching_rect" : [ 36.0, 764.0, 34.0, 22.0 ],
					"text" : "sel 1"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-30",
					"maxclass" : "toggle",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "int" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 36.0, 640.0, 85.949995636940002, 85.949995636940002 ],
					"presentation" : 1,
					"presentation_rect" : [ 484.000007212162018, 288.800004303455353, 74.999998927116394, 74.999998927116394 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-20",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 36.0, 904.0, 26.0, 26.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontsize" : 20.0,
					"id" : "obj-46",
					"linecount" : 2,
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 36.0, 587.0, 61.0, 51.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 481.600007176399231, 254.400003790855408, 80.000001192092896, 29.0 ],
					"text" : "On / Off"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-42",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 36.0, 809.0, 27.799997091293335, 27.799997091293335 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-32",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 0,
					"patching_rect" : [ 574.0, 967.0, 35.0, 22.0 ],
					"text" : "dac~"
				}

			}
, 			{
				"box" : 				{
					"fontface" : 0,
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"id" : "obj-11",
					"maxclass" : "number~",
					"mode" : 2,
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "signal", "float" ],
					"patching_rect" : [ 422.0, 997.0, 56.0, 22.0 ],
					"sig" : 0.0
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-38",
					"maxclass" : "toggle",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "int" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 860.0, 536.0, 25.299997091293335, 25.299997091293335 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-35",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "signal" ],
					"patching_rect" : [ 428.0, 957.0, 69.0, 22.0 ],
					"text" : "sfrecord~ 2"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-34",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 36.0, 856.0, 80.0, 22.0 ],
					"text" : "open out.wav"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-28",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 738.0, 173.5, 137.0, 22.0 ],
					"text" : "0."
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-52",
					"linecount" : 2,
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1167.5, 194.0, 90.0, 33.0 ],
					"text" : "novelify all dimensions"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-50",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "bang", "" ],
					"patching_rect" : [ 1334.5, 134.0, 34.0, 22.0 ],
					"text" : "sel 1"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-49",
					"linecount" : 4,
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 1277.5, 192.0, 659.0, 62.0 ],
					"text" : "1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-47",
					"linecount" : 4,
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 1120.5, 168.0, 649.0, 62.0 ],
					"text" : "1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-41",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "bang", "" ],
					"patching_rect" : [ 1253.5, 122.0, 34.0, 22.0 ],
					"text" : "sel 0"
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontsize" : 12.0,
					"id" : "obj-36",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1315.0, 34.5, 169.0, 20.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 266.5, 133.0, 131.0, 20.0 ],
					"text" : "Novelification Mode"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-31",
					"linecount" : 3,
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1391.0, 242.0, 102.0, 47.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 687.75, 126.200001895427704, 151.5, 20.0 ],
					"text" : "custom novelification ratio"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-24",
					"linecount" : 2,
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1277.5, 213.0, 97.0, 33.0 ],
					"text" : "only novelify dimension 0"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-40",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 561.5, 261.0, 210.5, 22.0 ],
					"text" : "vexpr $f1 * $f2"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-33",
					"linecount" : 4,
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 1153.0, 297.0, 649.0, 62.0 ],
					"text" : "1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1"
				}

			}
, 			{
				"box" : 				{
					"fontsize" : 9.144710682867041,
					"id" : "obj-27",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 656.0, 403.0, 148.0, 17.0 ],
					"presentation" : 1,
					"presentation_linecount" : 2,
					"presentation_rect" : [ 427.000004887580872, 288.800004303455353, 45.60000067949295, 27.0 ],
					"text" : "Latent Gain:"
				}

			}
, 			{
				"box" : 				{
					"fontface" : 1,
					"fontsize" : 12.0,
					"id" : "obj-25",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 796.0, 47.0, 209.0, 20.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 266.300004899501801, 215.0, 125.0, 20.0 ],
					"text" : "Novelification Ratio",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-23",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 390.200002908706665, 503.0, 244.0, 22.0 ],
					"text" : "vexpr $f1 * $f2 @scalarmode 1"
				}

			}
, 			{
				"box" : 				{
					"floatoutput" : 1,
					"id" : "obj-22",
					"maxclass" : "dial",
					"mult" : 0.01,
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "float" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 611.0, 398.0, 40.0, 40.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 427.000004887580872, 317.600004732608795, 45.60000067949295, 45.60000067949295 ],
					"size" : 200.0,
					"varname" : "dial"
				}

			}
, 			{
				"box" : 				{
					"candycane" : 4,
					"id" : "obj-16",
					"maxclass" : "multislider",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 493.0, 577.0, 72.0, 56.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 99.0, 275.200004100799561, 315.0, 88.0 ],
					"setminmax" : [ -4.0, 4.0 ],
					"size" : 64,
					"spacing" : 2,
					"thickness" : 4
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-14",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 390.200002908706665, 380.0, 193.799997091293335, 22.0 ],
					"text" : "vexpr $f1 + $f2"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-13",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 310.0, 183.5, 199.0, 22.0 ],
					"text" : "vexpr $f1 * (1 - $f2) @scalarmode 1"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-12",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 561.5, 214.0, 173.0, 22.0 ],
					"text" : "vexpr $f1 * $f2 @scalarmode 1"
				}

			}
, 			{
				"box" : 				{
					"floatoutput" : 1,
					"id" : "obj-7",
					"maxclass" : "slider",
					"mult" : 0.005,
					"numinlets" : 1,
					"numoutlets" : 1,
					"orientation" : 1,
					"outlettype" : [ "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 796.0, 103.0, 123.0, 20.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 267.200003981590271, 190.199999690055847, 123.200001835823059, 20.800000309944153 ],
					"size" : 200.0
				}

			}
, 			{
				"box" : 				{
					"candycane" : 4,
					"id" : "obj-2",
					"maxclass" : "multislider",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 595.0, 290.0, 85.0, 72.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 412.000006139278412, 113.0, 147.0, 98.0 ],
					"setminmax" : [ -4.0, 4.0 ],
					"size" : 64,
					"spacing" : 2,
					"thickness" : 4
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-3",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"patching_rect" : [ 634.0, 55.0, 101.0, 22.0 ],
					"text" : "route /emb_novel"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-4",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 649.0, 103.0, 71.0, 22.0 ],
					"text" : "fromsymbol"
				}

			}
, 			{
				"box" : 				{
					"candycane" : 4,
					"id" : "obj-21",
					"maxclass" : "multislider",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 420.0, 214.0, 89.0, 67.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 99.0, 112.0, 147.0, 100.0 ],
					"setminmax" : [ -4.0, 4.0 ],
					"size" : 64,
					"spacing" : 2,
					"thickness" : 4
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-18",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"patching_rect" : [ 436.0, 55.0, 66.0, 22.0 ],
					"text" : "route /emb"
				}

			}
, 			{
				"box" : 				{
					"fontface" : 0,
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"id" : "obj-70",
					"maxclass" : "number~",
					"mode" : 2,
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "signal", "float" ],
					"patching_rect" : [ 471.0, 846.0, 56.0, 22.0 ],
					"sig" : 0.0
				}

			}
, 			{
				"box" : 				{
					"attr" : "gpu",
					"id" : "obj-17",
					"maxclass" : "attrui",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 860.0, 656.0, 150.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"attr" : "enable_model",
					"id" : "obj-15",
					"maxclass" : "attrui",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 860.0, 581.0, 150.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-9",
					"maxclass" : "newobj",
					"numinlets" : 256,
					"numoutlets" : 2,
					"outlettype" : [ "signal", "signal" ],
					"patching_rect" : [ 585.0, 846.0, 680.5, 22.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 99.0, 394.0, 205.428595185279846, 22.0 ],
					"text" : "nn~ same-s-nn-tilde decode 8192",
					"varname" : "decoder"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-63",
					"linecount" : 6,
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "multichannelsignal" ],
					"patching_rect" : [ 585.0, 699.0, 1060.0, 89.0 ],
					"text" : "mc.list~ 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251 252 253 254 255 256"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-8",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 256,
					"outlettype" : [ "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal", "signal" ],
					"patching_rect" : [ 585.0, 748.0, 680.5, 22.0 ],
					"text" : "mc.unpack~ 256",
					"varname" : "mc"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-5",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 436.0, 96.999999284744263, 71.0, 22.0 ],
					"text" : "fromsymbol"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-1",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 515.0, 9.0, 97.0, 22.0 ],
					"text" : "udpreceive 7004"
				}

			}
 ],
		"lines" : [ 			{
				"patchline" : 				{
					"destination" : [ "obj-18", 0 ],
					"order" : 1,
					"source" : [ "obj-1", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-26", 0 ],
					"order" : 2,
					"source" : [ "obj-1", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-3", 0 ],
					"order" : 0,
					"source" : [ "obj-1", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-60", 0 ],
					"source" : [ "obj-10", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-40", 0 ],
					"source" : [ "obj-12", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-153", 0 ],
					"source" : [ "obj-124", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-14", 0 ],
					"source" : [ "obj-13", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-23", 0 ],
					"order" : 1,
					"source" : [ "obj-14", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-45", 0 ],
					"order" : 0,
					"source" : [ "obj-14", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 0 ],
					"source" : [ "obj-15", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-74", 0 ],
					"source" : [ "obj-153", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 0 ],
					"source" : [ "obj-17", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-5", 0 ],
					"source" : [ "obj-18", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-65", 0 ],
					"source" : [ "obj-19", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-38", 0 ],
					"source" : [ "obj-20", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-45", 1 ],
					"source" : [ "obj-22", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-16", 0 ],
					"order" : 1,
					"source" : [ "obj-23", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-63", 0 ],
					"order" : 0,
					"source" : [ "obj-23", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-30", 0 ],
					"order" : 1,
					"source" : [ "obj-26", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-61", 0 ],
					"order" : 0,
					"source" : [ "obj-26", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-12", 1 ],
					"order" : 1,
					"source" : [ "obj-28", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-13", 1 ],
					"order" : 2,
					"source" : [ "obj-28", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-33", 0 ],
					"order" : 0,
					"source" : [ "obj-28", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-7", 0 ],
					"source" : [ "obj-29", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-4", 0 ],
					"source" : [ "obj-3", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-53", 0 ],
					"source" : [ "obj-30", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-40", 1 ],
					"source" : [ "obj-33", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-20", 0 ],
					"order" : 1,
					"source" : [ "obj-34", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 0 ],
					"order" : 0,
					"source" : [ "obj-34", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-11", 0 ],
					"source" : [ "obj-35", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-15", 0 ],
					"order" : 0,
					"source" : [ "obj-38", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-32", 0 ],
					"order" : 1,
					"source" : [ "obj-38", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 0 ],
					"order" : 2,
					"source" : [ "obj-38", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-22", 0 ],
					"source" : [ "obj-39", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-12", 0 ],
					"order" : 2,
					"source" : [ "obj-4", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-2", 0 ],
					"order" : 1,
					"source" : [ "obj-4", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-28", 0 ],
					"order" : 0,
					"source" : [ "obj-4", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-14", 1 ],
					"order" : 1,
					"source" : [ "obj-40", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-51", 0 ],
					"order" : 0,
					"source" : [ "obj-40", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-47", 0 ],
					"source" : [ "obj-41", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-50", 0 ],
					"source" : [ "obj-41", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-34", 0 ],
					"source" : [ "obj-42", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-48", 0 ],
					"source" : [ "obj-43", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-48", 0 ],
					"source" : [ "obj-44", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-23", 1 ],
					"source" : [ "obj-45", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-33", 1 ],
					"source" : [ "obj-47", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-33", 1 ],
					"source" : [ "obj-49", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-13", 0 ],
					"order" : 1,
					"source" : [ "obj-5", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-21", 0 ],
					"order" : 0,
					"source" : [ "obj-5", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-49", 0 ],
					"source" : [ "obj-50", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-73", 0 ],
					"source" : [ "obj-50", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-38", 0 ],
					"source" : [ "obj-53", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-42", 0 ],
					"source" : [ "obj-53", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-33", 1 ],
					"source" : [ "obj-60", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-58", 0 ],
					"source" : [ "obj-61", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-8", 0 ],
					"source" : [ "obj-63", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-67", 0 ],
					"source" : [ "obj-65", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-71", 0 ],
					"source" : [ "obj-67", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-28", 1 ],
					"source" : [ "obj-7", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-41", 0 ],
					"source" : [ "obj-71", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-10", 0 ],
					"source" : [ "obj-73", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-70", 0 ],
					"order" : 1,
					"source" : [ "obj-8", 3 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 255 ],
					"source" : [ "obj-8", 255 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 254 ],
					"source" : [ "obj-8", 254 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 253 ],
					"source" : [ "obj-8", 253 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 252 ],
					"source" : [ "obj-8", 252 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 251 ],
					"source" : [ "obj-8", 251 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 250 ],
					"source" : [ "obj-8", 250 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 249 ],
					"source" : [ "obj-8", 249 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 248 ],
					"source" : [ "obj-8", 248 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 247 ],
					"source" : [ "obj-8", 247 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 246 ],
					"source" : [ "obj-8", 246 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 245 ],
					"source" : [ "obj-8", 245 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 244 ],
					"source" : [ "obj-8", 244 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 243 ],
					"source" : [ "obj-8", 243 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 242 ],
					"source" : [ "obj-8", 242 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 241 ],
					"source" : [ "obj-8", 241 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 240 ],
					"source" : [ "obj-8", 240 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 239 ],
					"source" : [ "obj-8", 239 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 238 ],
					"source" : [ "obj-8", 238 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 237 ],
					"source" : [ "obj-8", 237 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 236 ],
					"source" : [ "obj-8", 236 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 235 ],
					"source" : [ "obj-8", 235 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 234 ],
					"source" : [ "obj-8", 234 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 233 ],
					"source" : [ "obj-8", 233 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 232 ],
					"source" : [ "obj-8", 232 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 231 ],
					"source" : [ "obj-8", 231 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 230 ],
					"source" : [ "obj-8", 230 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 229 ],
					"source" : [ "obj-8", 229 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 228 ],
					"source" : [ "obj-8", 228 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 227 ],
					"source" : [ "obj-8", 227 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 226 ],
					"source" : [ "obj-8", 226 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 225 ],
					"source" : [ "obj-8", 225 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 224 ],
					"source" : [ "obj-8", 224 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 223 ],
					"source" : [ "obj-8", 223 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 222 ],
					"source" : [ "obj-8", 222 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 221 ],
					"source" : [ "obj-8", 221 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 220 ],
					"source" : [ "obj-8", 220 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 219 ],
					"source" : [ "obj-8", 219 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 218 ],
					"source" : [ "obj-8", 218 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 217 ],
					"source" : [ "obj-8", 217 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 216 ],
					"source" : [ "obj-8", 216 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 215 ],
					"source" : [ "obj-8", 215 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 214 ],
					"source" : [ "obj-8", 214 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 213 ],
					"source" : [ "obj-8", 213 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 212 ],
					"source" : [ "obj-8", 212 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 211 ],
					"source" : [ "obj-8", 211 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 210 ],
					"source" : [ "obj-8", 210 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 209 ],
					"source" : [ "obj-8", 209 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 208 ],
					"source" : [ "obj-8", 208 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 207 ],
					"source" : [ "obj-8", 207 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 206 ],
					"source" : [ "obj-8", 206 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 205 ],
					"source" : [ "obj-8", 205 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 204 ],
					"source" : [ "obj-8", 204 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 203 ],
					"source" : [ "obj-8", 203 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 202 ],
					"source" : [ "obj-8", 202 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 201 ],
					"source" : [ "obj-8", 201 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 200 ],
					"source" : [ "obj-8", 200 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 199 ],
					"source" : [ "obj-8", 199 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 198 ],
					"source" : [ "obj-8", 198 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 197 ],
					"source" : [ "obj-8", 197 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 196 ],
					"source" : [ "obj-8", 196 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 195 ],
					"source" : [ "obj-8", 195 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 194 ],
					"source" : [ "obj-8", 194 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 193 ],
					"source" : [ "obj-8", 193 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 192 ],
					"source" : [ "obj-8", 192 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 191 ],
					"source" : [ "obj-8", 191 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 190 ],
					"source" : [ "obj-8", 190 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 189 ],
					"source" : [ "obj-8", 189 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 188 ],
					"source" : [ "obj-8", 188 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 187 ],
					"source" : [ "obj-8", 187 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 186 ],
					"source" : [ "obj-8", 186 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 185 ],
					"source" : [ "obj-8", 185 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 184 ],
					"source" : [ "obj-8", 184 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 183 ],
					"source" : [ "obj-8", 183 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 182 ],
					"source" : [ "obj-8", 182 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 181 ],
					"source" : [ "obj-8", 181 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 180 ],
					"source" : [ "obj-8", 180 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 179 ],
					"source" : [ "obj-8", 179 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 178 ],
					"source" : [ "obj-8", 178 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 177 ],
					"source" : [ "obj-8", 177 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 176 ],
					"source" : [ "obj-8", 176 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 175 ],
					"source" : [ "obj-8", 175 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 174 ],
					"source" : [ "obj-8", 174 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 173 ],
					"source" : [ "obj-8", 173 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 172 ],
					"source" : [ "obj-8", 172 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 171 ],
					"source" : [ "obj-8", 171 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 170 ],
					"source" : [ "obj-8", 170 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 169 ],
					"source" : [ "obj-8", 169 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 168 ],
					"source" : [ "obj-8", 168 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 167 ],
					"source" : [ "obj-8", 167 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 166 ],
					"source" : [ "obj-8", 166 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 165 ],
					"source" : [ "obj-8", 165 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 164 ],
					"source" : [ "obj-8", 164 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 163 ],
					"source" : [ "obj-8", 163 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 162 ],
					"source" : [ "obj-8", 162 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 161 ],
					"source" : [ "obj-8", 161 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 160 ],
					"source" : [ "obj-8", 160 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 159 ],
					"source" : [ "obj-8", 159 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 158 ],
					"source" : [ "obj-8", 158 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 157 ],
					"source" : [ "obj-8", 157 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 156 ],
					"source" : [ "obj-8", 156 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 155 ],
					"source" : [ "obj-8", 155 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 154 ],
					"source" : [ "obj-8", 154 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 153 ],
					"source" : [ "obj-8", 153 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 152 ],
					"source" : [ "obj-8", 152 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 151 ],
					"source" : [ "obj-8", 151 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 150 ],
					"source" : [ "obj-8", 150 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 149 ],
					"source" : [ "obj-8", 149 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 148 ],
					"source" : [ "obj-8", 148 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 147 ],
					"source" : [ "obj-8", 147 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 146 ],
					"source" : [ "obj-8", 146 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 145 ],
					"source" : [ "obj-8", 145 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 144 ],
					"source" : [ "obj-8", 144 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 143 ],
					"source" : [ "obj-8", 143 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 142 ],
					"source" : [ "obj-8", 142 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 141 ],
					"source" : [ "obj-8", 141 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 140 ],
					"source" : [ "obj-8", 140 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 139 ],
					"source" : [ "obj-8", 139 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 138 ],
					"source" : [ "obj-8", 138 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 137 ],
					"source" : [ "obj-8", 137 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 136 ],
					"source" : [ "obj-8", 136 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 135 ],
					"source" : [ "obj-8", 135 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 134 ],
					"source" : [ "obj-8", 134 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 133 ],
					"source" : [ "obj-8", 133 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 132 ],
					"source" : [ "obj-8", 132 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 131 ],
					"source" : [ "obj-8", 131 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 130 ],
					"source" : [ "obj-8", 130 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 129 ],
					"source" : [ "obj-8", 129 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 128 ],
					"source" : [ "obj-8", 128 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 127 ],
					"source" : [ "obj-8", 127 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 126 ],
					"source" : [ "obj-8", 126 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 125 ],
					"source" : [ "obj-8", 125 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 124 ],
					"source" : [ "obj-8", 124 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 123 ],
					"source" : [ "obj-8", 123 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 122 ],
					"source" : [ "obj-8", 122 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 121 ],
					"source" : [ "obj-8", 121 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 120 ],
					"source" : [ "obj-8", 120 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 119 ],
					"source" : [ "obj-8", 119 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 118 ],
					"source" : [ "obj-8", 118 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 117 ],
					"source" : [ "obj-8", 117 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 116 ],
					"source" : [ "obj-8", 116 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 115 ],
					"source" : [ "obj-8", 115 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 114 ],
					"source" : [ "obj-8", 114 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 113 ],
					"source" : [ "obj-8", 113 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 112 ],
					"source" : [ "obj-8", 112 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 111 ],
					"source" : [ "obj-8", 111 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 110 ],
					"source" : [ "obj-8", 110 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 109 ],
					"source" : [ "obj-8", 109 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 108 ],
					"source" : [ "obj-8", 108 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 107 ],
					"source" : [ "obj-8", 107 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 106 ],
					"source" : [ "obj-8", 106 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 105 ],
					"source" : [ "obj-8", 105 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 104 ],
					"source" : [ "obj-8", 104 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 103 ],
					"source" : [ "obj-8", 103 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 102 ],
					"source" : [ "obj-8", 102 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 101 ],
					"source" : [ "obj-8", 101 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 100 ],
					"source" : [ "obj-8", 100 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 99 ],
					"source" : [ "obj-8", 99 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 98 ],
					"source" : [ "obj-8", 98 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 97 ],
					"source" : [ "obj-8", 97 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 96 ],
					"source" : [ "obj-8", 96 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 95 ],
					"source" : [ "obj-8", 95 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 94 ],
					"source" : [ "obj-8", 94 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 93 ],
					"source" : [ "obj-8", 93 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 92 ],
					"source" : [ "obj-8", 92 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 91 ],
					"source" : [ "obj-8", 91 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 90 ],
					"source" : [ "obj-8", 90 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 89 ],
					"source" : [ "obj-8", 89 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 88 ],
					"source" : [ "obj-8", 88 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 87 ],
					"source" : [ "obj-8", 87 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 86 ],
					"source" : [ "obj-8", 86 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 85 ],
					"source" : [ "obj-8", 85 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 84 ],
					"source" : [ "obj-8", 84 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 83 ],
					"source" : [ "obj-8", 83 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 82 ],
					"source" : [ "obj-8", 82 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 81 ],
					"source" : [ "obj-8", 81 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 80 ],
					"source" : [ "obj-8", 80 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 79 ],
					"source" : [ "obj-8", 79 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 78 ],
					"source" : [ "obj-8", 78 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 77 ],
					"source" : [ "obj-8", 77 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 76 ],
					"source" : [ "obj-8", 76 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 75 ],
					"source" : [ "obj-8", 75 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 74 ],
					"source" : [ "obj-8", 74 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 73 ],
					"source" : [ "obj-8", 73 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 72 ],
					"source" : [ "obj-8", 72 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 71 ],
					"source" : [ "obj-8", 71 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 70 ],
					"source" : [ "obj-8", 70 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 69 ],
					"source" : [ "obj-8", 69 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 68 ],
					"source" : [ "obj-8", 68 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 67 ],
					"source" : [ "obj-8", 67 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 66 ],
					"source" : [ "obj-8", 66 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 65 ],
					"source" : [ "obj-8", 65 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 64 ],
					"source" : [ "obj-8", 64 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 63 ],
					"source" : [ "obj-8", 63 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 62 ],
					"source" : [ "obj-8", 62 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 61 ],
					"source" : [ "obj-8", 61 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 60 ],
					"source" : [ "obj-8", 60 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 59 ],
					"source" : [ "obj-8", 59 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 58 ],
					"source" : [ "obj-8", 58 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 57 ],
					"source" : [ "obj-8", 57 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 56 ],
					"source" : [ "obj-8", 56 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 55 ],
					"source" : [ "obj-8", 55 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 54 ],
					"source" : [ "obj-8", 54 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 53 ],
					"source" : [ "obj-8", 53 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 52 ],
					"source" : [ "obj-8", 52 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 51 ],
					"source" : [ "obj-8", 51 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 50 ],
					"source" : [ "obj-8", 50 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 49 ],
					"source" : [ "obj-8", 49 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 48 ],
					"source" : [ "obj-8", 48 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 47 ],
					"source" : [ "obj-8", 47 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 46 ],
					"source" : [ "obj-8", 46 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 45 ],
					"source" : [ "obj-8", 45 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 44 ],
					"source" : [ "obj-8", 44 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 43 ],
					"source" : [ "obj-8", 43 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 42 ],
					"source" : [ "obj-8", 42 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 41 ],
					"source" : [ "obj-8", 41 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 40 ],
					"source" : [ "obj-8", 40 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 39 ],
					"source" : [ "obj-8", 39 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 38 ],
					"source" : [ "obj-8", 38 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 37 ],
					"source" : [ "obj-8", 37 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 36 ],
					"source" : [ "obj-8", 36 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 35 ],
					"source" : [ "obj-8", 35 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 34 ],
					"source" : [ "obj-8", 34 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 33 ],
					"source" : [ "obj-8", 33 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 32 ],
					"source" : [ "obj-8", 32 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 31 ],
					"source" : [ "obj-8", 31 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 30 ],
					"source" : [ "obj-8", 30 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 29 ],
					"source" : [ "obj-8", 29 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 28 ],
					"source" : [ "obj-8", 28 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 27 ],
					"source" : [ "obj-8", 27 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 26 ],
					"source" : [ "obj-8", 26 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 25 ],
					"source" : [ "obj-8", 25 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 24 ],
					"source" : [ "obj-8", 24 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 23 ],
					"source" : [ "obj-8", 23 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 22 ],
					"source" : [ "obj-8", 22 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 21 ],
					"source" : [ "obj-8", 21 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 20 ],
					"source" : [ "obj-8", 20 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 19 ],
					"source" : [ "obj-8", 19 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 18 ],
					"source" : [ "obj-8", 18 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 17 ],
					"source" : [ "obj-8", 17 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 16 ],
					"source" : [ "obj-8", 16 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 15 ],
					"source" : [ "obj-8", 15 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 14 ],
					"source" : [ "obj-8", 14 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 13 ],
					"source" : [ "obj-8", 13 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 12 ],
					"source" : [ "obj-8", 12 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 11 ],
					"source" : [ "obj-8", 11 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 10 ],
					"source" : [ "obj-8", 10 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 9 ],
					"source" : [ "obj-8", 9 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 8 ],
					"source" : [ "obj-8", 8 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 7 ],
					"source" : [ "obj-8", 7 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 6 ],
					"source" : [ "obj-8", 6 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 5 ],
					"source" : [ "obj-8", 5 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 4 ],
					"source" : [ "obj-8", 4 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 3 ],
					"order" : 0,
					"source" : [ "obj-8", 3 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 2 ],
					"source" : [ "obj-8", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 1 ],
					"source" : [ "obj-8", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 0 ],
					"source" : [ "obj-8", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-32", 1 ],
					"order" : 0,
					"source" : [ "obj-9", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-32", 0 ],
					"order" : 0,
					"source" : [ "obj-9", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 1 ],
					"order" : 1,
					"source" : [ "obj-9", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 0 ],
					"order" : 1,
					"source" : [ "obj-9", 0 ]
				}

			}
 ],
		"dependency_cache" : [ 			{
				"name" : "nn~.mxo",
				"type" : "iLaX"
			}
 ],
		"autosave" : 0
	}

}
