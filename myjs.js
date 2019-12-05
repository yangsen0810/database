function onView(pid, bid, pname, verifycode) {
			var url = "" + "/fcjadpater/select/NET_YSXK_PIC?sseq=" + bid;
			$.ajax({
				async: true,
				url: url,
				method: "post",
				data: {

				},
				dataType: "json",
				success: function (jsonData) {
					if (jsonData == null) {
						alert("网络异常，请重试!");
						return;
					}

					if (jsonData.rows != null) {
						var i = 0;
						var rows = null;

						if (typeof (jsonData.rows) == "string") {
							var t = (jsonData.rows == "" || jsonData.rows == null) ? "[]" : jsonData.rows;
							rows = eval("(" + t + ")");
						} else {
							rows = jsonData.rows;
						}

						var html = "";
						var total = jsonData.total;
						if (total > 0) {
							html = "<div><h1 class='xmxx'><a href=\"javascript:showProject('" + pid + "','" +
								verifycode + "');\">点击查看【" + pname + "】项目信息</a></h1></div>";
							for (i = 0; i < rows.length; i++) {
								var row = rows[i];
								var fpath = row.fpath;
								if (fpath != null && fpath != "") {
									var img = PIC_SERVER_PREFIX + fpath;
									html += "<div style=\"text-align:center;\"><img width=\"90%\" src=\"" + img +
										"\" border=\"0\"></div>"
								}
							}
						} else {
							html = "<div><h1 class='xmxx'><a href=\"javascript:showProject('" + pid + "','" +
								verifycode + "');\">点击查看【" + pname + "】项目信息</a></h1></div>";
							html += "<div style=\"text-align:center;\"><h1 class='xmxx'>暂无图片数据</h1></div>"
						}

						layer.open({
							closeBtn: 1,
							type: 1,
							area: ['900px', '450px'],
							title: '预售许可详情',
							moveType: 1,
							shadeClose: true,
							content: html
						});
					} else if (jsonData.message != null && jsonData.message != "") {
						alert(jsonData.message);
						return;
					} else {
						alert("数据结果读取错误，请重试!");
					}
				}
			});
		}
