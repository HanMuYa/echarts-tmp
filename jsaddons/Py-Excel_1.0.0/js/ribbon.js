// 字符串变hash
function hash32(str) {
  let h = 2166136261; // FNV-1a 32 位偏移常量起点
  for (let i = 0; i < str.length; i++) {
    h ^= str.charCodeAt(i);
    h += (h << 1) + (h << 4) + (h << 7) + (h << 8) + (h << 24);
  }
  // 转为无符号 32 位
  return h >>> 0;
}

let allpanel = {};  // 用来储存侧边栏id

//这个函数在整个wps加载项中是第一个执行的
function OnAddinLoad(ribbonUI){
    if (typeof (window.Application.ribbonUI) != "object"){
		window.Application.ribbonUI = ribbonUI
    }
    
    if (typeof (window.Application.Enum) != "object") { // 如果没有内置枚举值
        window.Application.Enum = WPS_Enum
    }

    window.Application.PluginStorage.setItem("EnableFlag", false) //往PluginStorage中设置一个标记，用于控制两个按钮的置灰
    window.Application.PluginStorage.setItem("ApiEventFlag", false) //往PluginStorage中设置一个标记，用于控制ApiEvent的按钮label
	
    return true
}

var WebNotifycount = 0;
function OnAction(control) {
    const eleId = control.Id
    switch (eleId) {
        case "py":
			{
				let workbook = window.Application.ActiveWorkbook; // 获取workbook完整路径
				let tsId = window.Application.PluginStorage.getItem(`py_taskpane_id_${hash32(workbook.FullName)}`);
                if (!tsId) {
                    let tskpane = window.Application.CreateTaskPane(GetUrlPath() + "/ui/python.html")
                    let id = tskpane.ID
                    window.Application.PluginStorage.setItem(`py_taskpane_id_${hash32(workbook.FullName)}`, id)
                    tskpane.Visible = true
					tskpane.width = 800
					allpanel[`py_taskpane_id_${hash32(workbook.FullName)}`] = true
                } else {
                    let tskpane = window.Application.GetTaskPane(tsId)
                    tskpane.Visible = !tskpane.Visible
					allpanel[`py_taskpane_id_${hash32(workbook.FullName)}`] = !allpanel[`py_taskpane_id_${hash32(workbook.FullName)}`]
                }
			}
			break
        case "func":
			{
				let workbook = window.Application.ActiveWorkbook; // 获取workbook完整路径
				let tsId = window.Application.PluginStorage.getItem(`func_taskpane_id_${hash32(workbook.FullName)}`);
                if (!tsId) {
                    let tskpane = window.Application.CreateTaskPane(GetUrlPath() + "/ui/func.html")
                    let id = tskpane.ID
                    window.Application.PluginStorage.setItem(`func_taskpane_id_${hash32(workbook.FullName)}`, id)
                    tskpane.Visible = true
					tskpane.width = 800
					allpanel[`func_taskpane_id_${hash32(workbook.FullName)}`] = true
                } else {
                    let tskpane = window.Application.GetTaskPane(tsId)
                    tskpane.Visible = !tskpane.Visible
					allpanel[`func_taskpane_id_${hash32(workbook.FullName)}`] = !allpanel[`func_taskpane_id_${hash32(workbook.FullName)}`]
                }
			}
			break
        default:
            break
    }
    return true
}

function GetImage(control) {
    const eleId = control.Id
    switch (eleId) {
        case "btnNotebook":
            return "images/notebook.svg"
        case "btnAi":
            return "images/ai.svg"
        case "btnManage":
            return "images/manage.svg"
        default:
            ;
    }
    return "images/newFromTemp.svg"
}

function OnGetEnabled(control) {
    const eleId = control.Id
    switch (eleId) {
        case "btnShowMsg":
            return true
            break
        case "btnShowDialog":
            {
                let bFlag = window.Application.PluginStorage.getItem("EnableFlag")
                return bFlag
                break
            }
        case "btnShowTaskPane":
            {
                let bFlag = window.Application.PluginStorage.getItem("EnableFlag")
                return bFlag
                break
            }
        default:
            break
    }
    return true
}

function OnGetVisible(control){
    return true
}

function OnGetLabel(control){
    const eleId = control.Id
    switch (eleId) {
        case "btnIsEnbable":
        {
            let bFlag = window.Application.PluginStorage.getItem("EnableFlag")
            return bFlag ?  "按钮Disable" : "按钮Enable"
            break
        }
        case "btnApiEvent":
        {
            let bFlag = window.Application.PluginStorage.getItem("ApiEventFlag")
            return bFlag ? "清除新建文件事件" : "注册新建文件事件"
            break
        }    
    }
    return ""
}

function OnNewDocumentApiEvent(doc){
    alert("新建文件事件响应，取文件名: " + doc.Name)
}

// 工作簿关闭
/* Application.ApiEvent.AddApiEventListener("WorkbookBeforeClose", function(workbook) {
	alert(123)
}); */

Application.ApiEvent.AddApiEventListener("WorkbookActivate", function(workbook) {
	setTimeout(() => {
	// let workbook = window.Application.ActiveWorkbook; // 获取workbook完整路径
	let x = [ 
		`py_taskpane_id_${hash32(workbook.FullName)}`,
        `func_taskpane_id_${hash32(workbook.FullName)}`,
	];
	let ID = null;
	let tskpane = null;
	for (const key in allpanel) {
		
		ID = window.Application.PluginStorage.getItem(key);
		if (!x.includes(key)) {
			tskpane = window.Application.GetTaskPane(ID);
            tskpane.Visible = false;
			tskpane = null;
		}
		else {
			if (ID) {
				tskpane = window.Application.GetTaskPane(ID);
				if (allpanel[key]) {
					tskpane.Visible = true;
				}
				else {
					tskpane.Visible = false;
				};
			};
			tskpane = null;
		};
	};
	}, 20); 
});

Application.ApiEvent.AddApiEventListener("AfterTaskPaneHidden", function() { 
    // 使用 setTimeout 延迟 50-100 毫秒执行
    setTimeout(() => {
        let workbook = window.Application.ActiveWorkbook;
        let x = [
			`py_taskpane_id_${hash32(workbook.FullName)}`,
            `func_taskpane_id_${hash32(workbook.FullName)}`,
        ];

        for (const key in allpanel) {
            let ID = window.Application.PluginStorage.getItem(key);
            if (x.includes(key)) {
                try {
                    let tskpane = window.Application.GetTaskPane(ID);
                    // 此时打印，Visible 应该是真实的 false 了
                    console.log(`关键Key: ${key}, 实时状态:`, tskpane.Visible);

                    // 既然是 AfterTaskPaneHidden 触发的，且 Visible 为 false
                    // 说明这个面板刚刚被用户手动点 X 关掉了
                    if (!tskpane.Visible) {
                        allpanel[key] = false; 
                        console.log("状态同步成功: 已将 allpanel 中的记录置为 false");
                    }
                } catch (e) {
                    // 如果面板被销毁导致报错，也说明它不在线了
                    allpanel[key] = false;
                }
            }
        }
    }, 20); 
});

window.Application.PluginStorage.setItem("url", GetUrlPath());
