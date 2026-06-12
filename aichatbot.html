import os
import json
import logging
import mimetypes
from flask import Flask, render_template_string, request, jsonify
import requests

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# ==================== DIFY 配置中心 ====================
DIFY_API_KEY = "app-ojb3NzazR84vHqxUyklB8i7e"  # 你的 API Key
DIFY_BASE_URL = "https://api.dify.ai"          # 本地私有化部署改类似 http://127.0.0.1
USER_ID = "rongjie"
DB_FILE = "conversations_db.json"
# ====================================================

# ==================== 本地轻量级对话数据库 ====================
def load_db():
    if not os.path.exists(DB_FILE):
        return {"sessions": []}
    try:
        with open(DB_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {"sessions": []}

def save_db(data):
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def update_session(conv_id, first_query, messages_list=None):
    db = load_db()
    exists = False
    for s in db["sessions"]:
        if s["id"] == conv_id:
            exists = True
            if messages_list is not None:
                s["messages"] = messages_list
            break
    if not exists and conv_id:
        title = first_query[:12] + "..." if len(first_query) > 12 else first_query
        db["sessions"].insert(0, {
            "id": conv_id,
            "title": title,
            "messages": messages_list or []
        })
    save_db(db)

# ==================== 前端 UI 对话 ====================
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QuantumFlow Earth-Terminal v14</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        
        body { 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, sans-serif;
            background: radial-gradient(circle at 50% 50%, #eef3f9 0%, #e2edf7 60%, #d8e5f3 100%);
            color: #1d1d1f;
            display: flex; 
            justify-content: center; 
            align-items: center; 
            height: 100vh;
            overflow: hidden;
            position: relative;
        }

        .line {
            border: none;
            height: 0.5px;
            background-color: rgba(0,0,0,0.05);
        }

        #canvas3d {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            z-index: 1;
            pointer-events: none;
        }
        
        /* 全局双栏全息底座 */
        .chat-container { 
            position: relative;
            z-index: 2;
            width: 95%; 
            max-width: 1250px; 
            height: 88vh; 
            
            background: rgba(255, 255, 255, 0.03) !important; 
            -webkit-backdrop-filter: blur(8px) saturate(140%) !important;
            backdrop-filter: blur(8px) saturate(140%) !important;
            
            transform: translateZ(0);
            -webkit-transform: translateZ(0);
            
            border-radius: 16px; 
            border: 1px solid rgba(255, 255, 255, 0.7);
            box-shadow: 0 50px 100px rgba(0, 30, 90, 0.04), 
                        0 2px 30px rgba(255, 255, 255, 0.5) inset; 
            display: flex; 
            overflow: hidden;
        }

        /* ==================== 🛠️ 左侧全息侧边栏 ==================== */
        .sidebar {
            width: 280px;
            background: rgba(240, 244, 250, 0.35);
            border-right: 1px solid rgba(0, 85, 255, 0.06);
            display: flex;
            flex-direction: column;
            flex-shrink: 0;
        }
        .sidebar-header {
            padding: 20px;
            flex-shrink: 0;
        }
        .new-chat-btn {
            width: 100%;
            background: rgba(255, 255, 255, 0.7);
            border: 1px solid rgba(0, 85, 255, 0.15);
            color: #0055ff;
            padding: 10px 16px;
            border-radius: 10px;
            font-weight: 600;
            font-size: 0.88rem;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            cursor: pointer;
            transition: all 0.2s cubic-bezier(0.25, 1, 0.5, 1);
            box-shadow: 0 2px 6px rgba(0, 85, 255, 0.04);
        }
        .new-chat-btn:hover {
            background: #0055ff;
            color: #ffffff;
            box-shadow: 0 4px 12px rgba(0, 85, 255, 0.2);
            border-color: #0055ff;
        }
        .history-list {
            flex: 1;
            overflow-y: auto;
            padding: 4px 12px;
            display: flex;
            flex-direction: column;
            gap: 6px;
        }
        .history-item {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 11px 14px;
            border-radius: 10px;
            cursor: pointer;
            color: #4e5969;
            font-size: 0.85rem;
            font-weight: 500;
            transition: all 0.2s;
            group: hover;
            position: relative;
            background: transparent;
            border: 1px solid transparent;
        }
        .history-item:hover {
            background: rgba(255, 255, 255, 0.5);
            color: #1d1d1f;
        }
        .history-item.active {
            background: rgba(0, 85, 255, 0.06);
            color: #0055ff;
            border-color: rgba(0, 85, 255, 0.1);
            font-weight: 600;
        }
        .history-item-title {
            display: flex;
            align-items: center;
            gap: 8px;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
            flex: 1;
        }
        .delete-session-btn {
            opacity: 0;
            background: transparent;
            border: none;
            color: #86868b;
            cursor: pointer;
            padding: 2px 6px;
            border-radius: 4px;
            transition: all 0.15s;
        }
        .history-item:hover .delete-session-btn {
            opacity: 1;
        }
        .delete-session-btn:hover {
            color: #ef4444;
            background: rgba(239, 68, 68, 0.08);
        }

        /* ==================== 右侧主视窗 ==================== */
        .main-chat {
            flex: 1;
            display: flex;
            flex-direction: column;
            overflow: hidden;
            background: transparent;
        }
        .chat-header { 
            background: rgba(255, 255, 255, 0.2) !important;
            padding: 20px 36px; 
            display: flex; 
            justify-content: space-between; 
            align-items: center; 
            border-bottom: 1px solid rgba(0, 85, 255, 0.04);
            flex-shrink: 0;
        }
        .header-title {
            font-size: 1rem; 
            font-weight: 700; 
            letter-spacing: 2.5px;
            text-transform: uppercase;
            color: #0055ff;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .status-dot {
            width: 6px; height: 6px;
            background: #00dd66; border-radius: 50%;
            box-shadow: 0 0 8px #00dd66;
        }
        .conv-tag { 
            font-family: monospace; font-size: 0.75rem; 
            background: rgba(0, 85, 255, 0.04); color: #0055ff;
            border: 1px solid rgba(0, 85, 255, 0.08);
            padding: 4px 12px; border-radius: 12px; 
        }

        .chat-messages { 
            flex: 1; padding: 36px 44px; 
            overflow-y: auto; display: flex; 
            flex-direction: column; gap: 30px; 
            background: transparent !important;
        }
        
        .message-wrapper {
            position: relative; display: flex;
            flex-direction: column; max-width: 75%;
        }
        .message-wrapper.user { align-self: flex-end; align-items: flex-end; }
        .message-wrapper.bot { align-self: flex-start; align-items: flex-start; }

        .message { 
            width: 100%; padding: 16px 22px; 
            font-size: 0.95rem; line-height: 1.68; 
            word-wrap: break-word; position: relative;
        }
        .message.user { 
            background: rgba(0, 85, 255, 0.05); color: #0044cc; 
            border-radius: 12px 12px 2px 12px; 
            border-right: 2.5px solid #0055ff; font-weight: 500;
            white-space: pre-wrap;
        }
        .message.bot { 
            background: rgba(255, 255, 255, 0.88); color: #1d1d1f; 
            border-radius: 12px 12px 12px 2px; 
            border-left: 3px solid #0055ff;
            box-shadow: 0 4px 16px rgba(0, 30, 90, 0.01);
        }
        
        .message-actions {
            display: flex; gap: 8px; margin-top: 4px;
            opacity: 0; transition: opacity 0.2s ease, transform 0.2s ease;
            transform: translateY(-2px); z-index: 5;
        }
        .message-wrapper:hover .message-actions { opacity: 1; transform: translateY(0); }
        .action-icon-btn {
            background: rgba(255, 255, 255, 0.8); border: 1px solid rgba(0, 85, 255, 0.1);
            color: #4e5969; border-radius: 6px; width: 26px; height: 26px;
            display: inline-flex; justify-content: center; align-items: center;
            cursor: pointer; font-size: 0.8rem; transition: all 0.15s ease;
        }
        .action-icon-btn:hover { background: #0055ff; color: #ffffff; border-color: #0055ff; }
        .action-icon-btn.copied { background: #00dd66 !important; color: white !important; border-color: #00dd66 !important; }

        .chat-input-wrapper {
            position: relative;
            background: rgba(255, 255, 255, 0.3) !important;
            border-top: 1px solid rgba(0, 85, 255, 0.06); 
            display: flex; flex-direction: column;
            min-height: 130px; max-height: 380px; height: 160px;     
            flex-shrink: 0; transition: border-color 0.25s ease;
        }
        .chat-input-wrapper.focused { border-top-color: rgba(0, 85, 255, 0.3); }

        .resize-bar {
            width: 100%; height: 8px; cursor: ns-resize; 
            position: absolute; top: -4px; left: 0; z-index: 10;
        }
        .resize-bar::after {
            content: ''; position: absolute; left: 0; right: 0; top: 3px; height: 1px;
            background: transparent; transition: background 0.2s;
        }
        .resize-bar:hover::after { background: rgba(0, 85, 255, 0.2); }

        .chat-textarea-container { flex: 1; padding: 16px 28px 0 28px; display: flex; }
        .chat-input { 
            flex: 1; height: 100%; border: none !important; outline: none !important;     
            background: transparent !important; color: #1d1d1f; font-size: 0.95rem; 
            line-height: 1.6; resize: none; font-family: inherit; overflow-y: auto; padding: 0;                                                   
        }

        .input-action-bar { padding: 6px 28px 14px 28px; display: flex; justify-content: space-between; align-items: center; }
        .action-left-zone { display: flex; align-items: center; gap: 12px; }

        .custom-select-wrapper { position: relative; display: inline-block; }
        .custom-select-wrapper i.prefix-icon {
            position: absolute; left: 12px; top: 50%; transform: translateY(-50%);
            color: #0055ff; font-size: 0.85rem; pointer-events: none; z-index: 2;
        }
        .beautiful-select {
            -webkit-appearance: none; -moz-appearance: none; appearance: none; 
            padding: 7px 32px 7px 32px; border: 1px solid rgba(0, 85, 255, 0.12); border-radius: 12px;
            background: rgba(255, 255, 255, 0.6); color: #1d1d1f; font-size: 0.8rem;
            font-weight: 600; outline: none; cursor: pointer; transition: all 0.25s ease;
        }
        .beautiful-select:hover { background: #ffffff; border-color: #0055ff; box-shadow: 0 2px 8px rgba(0, 85, 255, 0.08); }
        .custom-select-wrapper::after {
            content: "\\f282"; font-family: "bootstrap-icons"; position: absolute;
            right: 12px; top: 50%; transform: translateY(-50%); font-size: 0.65rem; color: #86868b; pointer-events: none;
        }

        .file-upload-input { display: none !important; }
        .custom-file-btn {
            display: inline-flex; align-items: center; gap: 6px; padding: 7px 14px;
            background: rgba(255, 255, 255, 0.6); color: #4e5969; border: 1px solid rgba(0, 85, 255, 0.12);
            border-radius: 12px; cursor: pointer; font-size: 0.8rem; font-weight: 600; transition: all 0.2s ease; user-select: none;
        }
        .custom-file-btn:hover { background: #ffffff; color: #0055ff; border-color: #0055ff; box-shadow: 0 2px 8px rgba(0, 85, 255, 0.08); }
        .custom-file-btn.has-file { background: rgba(0, 221, 102, 0.06); color: #00aa44; border-color: rgba(0, 221, 102, 0.2); }
        .custom-file-btn.disabled { opacity: 0.4; cursor: not-allowed; background: rgba(0, 0, 0, 0.03) !important; color: #86868b !important; border-color: transparent !important; box-shadow: none !important; }

        .action-right-zone { display: flex; align-items: center; gap: 16px; }
        .input-tip { font-size: 0.75rem; color: #86868b; letter-spacing: 0.3px; }
        .send-btn { 
            display: inline-flex; align-items: center; gap: 8px; background: #0055ff; color: #ffffff; 
            border: none; padding: 8px 24px; border-radius: 12px; cursor: pointer; 
            font-weight: 600; font-size: 0.82rem; letter-spacing: 0.5px;
            box-shadow: 0 2px 8px rgba(0, 85, 255, 0.15); transition: all 0.2s;
        }
        .send-btn:hover { background: #0044cc; box-shadow: 0 4px 12px rgba(0, 68, 204, 0.25); }
        .send-btn:disabled { background: rgba(0, 0, 0, 0.05); color: #a1a1a6; box-shadow: none; cursor: not-allowed; }
        
        .tech-loading { display: inline-flex; gap: 4px; align-items: center; padding: 4px 0; }
        .tech-loading span { width: 3px; height: 12px; background: #0055ff; border-radius: 1px; animation: techWave 1.2s infinite ease-in-out; }
        .tech-loading span:nth-child(2) { animation-delay: 0.15s; }
        .tech-loading span:nth-child(3) { animation-delay: 0.3s; }
        @keyframes techWave { 0%, 100% { transform: scaleY(0.5); opacity: 0.3; } 50% { transform: scaleY(1.2); opacity: 1; } }

        ::-webkit-scrollbar { width: 4px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: rgba(0, 85, 255, 0.08); border-radius: 10px; }
    </style>
</head>
<body>

<div id="canvas3d"></div>

<div class="chat-container">
    <div class="sidebar">
        <div class="sidebar-header">
            <button class="new-chat-btn" id="newChatBtn">
                <i class="bi bi-plus-lg"></i>开启控制新对话
            </button>
        </div>
        <div class="history-list" id="historyList">
            </div>
    </div>

    <div class="main-chat">
        <div class="chat-header">
            <div class="header-title"><div class="status-dot"></div>DIFY智能体</div>
            <div class="conv-tag" id="convIdTag">SYS_STATUS: INTELLIGENT_FLOW</div>
        </div>

        <div class="chat-messages" id="chatMessages">
            </div>
        
        <div class="chat-input-wrapper" id="inputWrapper">
            <div class="resize-bar" id="resizeBar"></div>
            
            <div class="chat-textarea-container">
                <textarea id="userInput" class="chat-input" placeholder="输入控制对话指令... (支持回车换行)" rows="3"></textarea>
            </div>
            <hr class="line" />
            <div class="input-action-bar" style="margin-top: 10px;">
                
                <div class="action-left-zone">
                    <div class="custom-select-wrapper">
                        <i class="bi bi-translate prefix-icon"></i>
                        <select id="targetLang" class="beautiful-select">
                            <option value="中文">中文</option>
                            <option value="English">English</option>
                            <option value="日本語">日本語</option>
                        </select>
                    </div>

                    <label for="documentFile" class="custom-file-btn" id="customFileLabel">
                        <i class="bi bi-paperclip"></i>
                        <span id="fileBtnText">数据源</span>
                    </label>
                    <input type="file" id="documentFile" class="file-upload-input">
                </div>

                <div class="action-right-zone">
                    <span class="input-tip">换行: Enter | 发送: Shift+Enter</span>
                    <button id="sendBtn" class="send-btn">
                        <i class="bi bi-send"></i>
                        <span>发送</span>
                    </button>
                </div>
                
            </div>
        </div>
    </div>
</div>

<script>
    // ==================== THREE.JS 背景动画引擎 ====================
    let scene, camera, renderer, earthGroup;
    let flightLines = [];
    const maxFlightLines = 6;
    const earthRadius = 220;

    function init3D() {
        const container = document.getElementById('canvas3d');
        scene = new THREE.Scene();
        camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 1, 2000);
        camera.position.set(0, 0, 550);

        earthGroup = new THREE.Group();
        earthGroup.position.set(120, 0, -30); // 略微右偏，留出左侧边栏视觉空间
        scene.add(earthGroup);

        const particleCount = 3500; 
        const geometry = new THREE.BufferGeometry();
        const positions = new Float32Array(particleCount * 3);

        for (let i = 0; i < particleCount * 3; i += 3) {
            const u = Math.random(); const v = Math.random();
            const theta = u * 2.0 * Math.PI; const phi = Math.acos(2.0 * v - 1.0);
            positions[i] = earthRadius * Math.sin(phi) * Math.cos(theta);
            positions[i+1] = earthRadius * Math.sin(phi) * Math.sin(theta);
            positions[i+2] = earthRadius * Math.cos(phi);
        }

        geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
        const pMaterial = new THREE.PointsMaterial({
            color: 0x0055ff, size: 1.5, transparent: true, opacity: 0.06 
        });

        const earthParticles = new THREE.Points(geometry, pMaterial);
        earthGroup.add(earthParticles);

        renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
        renderer.setSize(window.innerWidth, window.innerHeight);
        container.appendChild(renderer.domElement);

        window.addEventListener('resize', onWindowResize, false);
        setInterval(createRandomFlightLine, 2000);
        animate();
    }

    function createRandomFlightLine() {
        if (flightLines.length >= maxFlightLines) {
            const oldLine = flightLines.shift();
            earthGroup.remove(oldLine.mesh);
        }
        const getSpherePoint = () => {
            const u = Math.random(); const v = Math.random();
            const theta = u * 2.0 * Math.PI; const phi = Math.acos(2.0 * v - 1.0);
            return new THREE.Vector3(
                earthRadius * Math.sin(phi) * Math.cos(theta),
                earthRadius * Math.sin(phi) * Math.sin(theta),
                earthRadius * Math.cos(phi)
            );
        };
        const startP = getSpherePoint(); const endP = getSpherePoint();
        if (startP.distanceTo(endP) < 180) return; 

        const midP = new THREE.Vector3().addVectors(startP, endP).multiplyScalar(0.5);
        const dist = startP.distanceTo(endP);
        midP.normalize().multiplyScalar(earthRadius + dist * 0.2); 

        const curve = new THREE.QuadraticBezierCurve3(startP, midP, endP);
        const curvePoints = curve.getPoints(50);
        const lineGeo = new THREE.BufferGeometry().setFromPoints(curvePoints);
        
        const lineMat = new THREE.LineBasicMaterial({ color: 0x00aaff, transparent: true, opacity: 0.15 });
        const lineMesh = new THREE.Line(lineGeo, lineMat);
        earthGroup.add(lineMesh);
        flightLines.push({ mesh: lineMesh, createdAt: Date.now() });
    }

    function animate() {
        requestAnimationFrame(animate);
        earthGroup.rotation.y += 0.0008;
        earthGroup.rotation.x += 0.0002;
        renderer.render(scene, camera);
    }

    function onWindowResize() {
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(window.innerWidth, window.innerHeight);
    }

    init3D();

    // ==================== 核心面板交互与对话挂载逻辑 ====================
    const inputWrapper = document.getElementById('inputWrapper');
    const resizeBar = document.getElementById('resizeBar');
    const userInput = document.getElementById('userInput');
    const chatMessages = document.getElementById('chatMessages');
    const documentFile = document.getElementById('documentFile');
    const customFileLabel = document.getElementById('customFileLabel');
    const fileBtnText = document.getElementById('fileBtnText');
    const historyList = document.getElementById('historyList');
    const newChatBtn = document.getElementById('newChatBtn');
    const sendBtn = document.getElementById('sendBtn');
    const targetLang = document.getElementById('targetLang');
    const convIdTag = document.getElementById('convIdTag');

    let currentConversationId = ""; 
    let isDragging = false;
    let startY = 0;
    let startHeight = 0;

    // 欢迎文本
    const WELCOME_TEXT = "全新无缝操控底座部署完毕。左侧已内嵌对话历史沙盒。语言配置模块与对话文件挂载组件已完全下沉整合至终端左下角。底层通信链路标准工业级状态正常。";

    // 初始化加载
    window.addEventListener('DOMContentLoaded', () => {
        loadHistoryList();
        initNewChat();
    });

    function initNewChat() {
        currentConversationId = "";
        convIdTag.innerText = "SYS_STATUS: INTELLIGENT_FLOW";
        chatMessages.innerHTML = "";
        appendMessageWrapper(WELCOME_TEXT, 'bot', false);
        unlockFileField();
        resetFileField();
        renderActiveSession();
    }

    function resetFileField() {
        documentFile.value = "";
        customFileLabel.classList.remove('has-file');
        customFileLabel.querySelector('i').className = "bi bi-paperclip";
        fileBtnText.innerText = '数据源';
    }

    function lockFileField() {
        documentFile.disabled = true; 
        customFileLabel.classList.add('disabled');
        customFileLabel.querySelector('i').className = "bi bi-lock";
        fileBtnText.innerText = '锁定';
    }

    function unlockFileField() {
        documentFile.disabled = false; 
        customFileLabel.classList.remove('disabled');
        customFileLabel.querySelector('i').className = "bi bi-paperclip";
        fileBtnText.innerText = '数据源';
    }

    documentFile.addEventListener('change', () => {
        if (documentFile.files.length > 0) {
            const fileName = documentFile.files[0].name;
            customFileLabel.classList.add('has-file');
            customFileLabel.querySelector('i').className = "bi bi-check-circle";
            fileBtnText.innerText = fileName.length > 10 ? fileName.substring(0,8)+'...' : fileName;
        } else {
            resetFileField();
        }
    });

    userInput.addEventListener('focus', () => { inputWrapper.classList.add('focused'); });
    userInput.addEventListener('blur', () => { inputWrapper.classList.remove('focused'); });

    // 面板高度拖拽拖拽线
    resizeBar.addEventListener('mousedown', (e) => {
        isDragging = true; startY = e.clientY; startHeight = inputWrapper.offsetHeight;
        document.body.style.cursor = 'ns-resize'; e.preventDefault();
    });

    document.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        const deltaY = startY - e.clientY;
        let newHeight = startHeight + deltaY;
        if (newHeight < 120) newHeight = 120;
        if (newHeight > 380) newHeight = 380;
        inputWrapper.style.height = newHeight + 'px';
    });

    document.addEventListener('mouseup', () => {
        if (isDragging) { isDragging = false; document.body.style.cursor = ''; }
    });

    userInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
            if (e.shiftKey || e.ctrlKey) {
                e.preventDefault(); sendMessage();      
            }
        }
    });

    function scrollToBottom() { chatMessages.scrollTop = chatMessages.scrollHeight; }

    function copyText(btn) {
        const wrapper = btn.closest('.message-wrapper');
        const text = wrapper.querySelector('.message').textContent;
        navigator.clipboard.writeText(text).then(() => {
            const icon = btn.querySelector('i');
            icon.className = "bi bi-check"; btn.classList.add('copied');
            setTimeout(() => { icon.className = "bi bi-copy"; btn.classList.remove('copied'); }, 1500);
        });
    }

    function editMessage(btn) {
        userInput.value = btn.closest('.message-wrapper').querySelector('.message').textContent;
        userInput.focus();
    }

    async function regenerateMessage(btn) {
        const wrapper = btn.closest('.message-wrapper');
        let prevUser = wrapper.previousElementSibling;
        while (prevUser && !prevUser.classList.contains('user')) {
            prevUser = prevUser.previousElementSibling;
        }
        if (!prevUser) return;
        await executeChatFlow(prevUser.querySelector('.message').textContent, wrapper);
    }

    function appendMessageWrapper(content, sender, isHtml = false) {
        const wrapper = document.createElement('div');
        wrapper.classList.add('message-wrapper', sender);

        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', sender);
        if (isHtml) messageDiv.innerHTML = content; else messageDiv.textContent = content; 
        wrapper.appendChild(messageDiv);

        const actionsDiv = document.createElement('div');
        actionsDiv.classList.add('message-actions');
        actionsDiv.innerHTML = `<button class="action-icon-btn" title="复制" onclick="copyText(this)"><i class="bi bi-copy"></i></button>`;

        if (sender === 'user') {
            actionsDiv.innerHTML += `<button class="action-icon-btn" title="编辑" onclick="editMessage(this)"><i class="bi bi-pencil-square"></i></button>`;
        } else if (sender === 'bot') {
            actionsDiv.innerHTML += `<button class="action-icon-btn" title="重试" onclick="regenerateMessage(this)"><i class="bi bi-arrow-clockwise"></i></button>`;
        }
        wrapper.appendChild(actionsDiv);
        chatMessages.appendChild(wrapper);
        scrollToBottom();
        return wrapper;
    }

    // ==================== 侧边栏与数据核心交互 ====================
    async function loadHistoryList() {
        try {
            const r = await fetch('/api/history');
            const data = await r.json();
            historyList.innerHTML = "";
            data.sessions.forEach(s => {
                const item = document.createElement('div');
                item.className = `history-item ${s.id === currentConversationId ? 'active' : ''}`;
                item.dataset.id = s.id;
                item.onclick = () => switchSession(s.id);
                
                item.innerHTML = `
                    <div class="history-item-title"><i class="bi bi-chat-left-text"></i><span>${s.title}</span></div>
                    <button class="delete-session-btn" title="核销会话" onclick="deleteSession(event, '${s.id}')">
                        <i class="bi bi-trash3"></i>
                    </button>
                `;
                historyList.appendChild(item);
            });
        } catch(e) { console.error("加载审计历史失败", e); }
    }

    function renderActiveSession() {
        document.querySelectorAll('.history-item').forEach(item => {
            if(item.dataset.id === currentConversationId) item.classList.add('active');
            else item.classList.remove('active');
        });
    }

    async function switchSession(convId) {
        if(convId === currentConversationId) return;
        try {
            const r = await fetch(`/api/history/${convId}`);
            if(!r.ok) return;
            const session = await r.json();
            
            currentConversationId = session.id;
            convIdTag.innerText = "CONV_ID: " + currentConversationId;
            chatMessages.innerHTML = "";
            
            if(session.messages && session.messages.length > 0) {
                session.messages.forEach(m => {
                    appendMessageWrapper(m.content, m.sender, m.sender === 'bot');
                });
                lockFileField();
            } else {
                appendMessageWrapper(WELCOME_TEXT, 'bot', false);
                unlockFileField();
            }
            renderActiveSession();
            resetFileField();
        } catch(e) { console.error("会话对话切流失败", e); }
    }

    async function deleteSession(event, convId) {
        event.stopPropagation();
        if(!confirm("确定核销并清除该核心控制对话会话吗？")) return;
        try {
            const r = await fetch(`/api/history/${convId}`, { method: 'DELETE' });
            if(r.ok) {
                if(currentConversationId === convId) { initNewChat(); }
                loadHistoryList();
            }
        } catch(e) { console.error("核销失败", e); }
    }

    newChatBtn.addEventListener('click', initNewChat);

    // 发送消息核心
    async function sendMessage() {
        const queryText = userInput.value.trim();
        if (!queryText) return;

        appendMessageWrapper(queryText, 'user', false);
        userInput.value = ''; 
        
        const botWrapper = appendMessageWrapper('<div class="tech-loading"><span></span><span></span><span></span></div>', 'bot', true);
        await executeChatFlow(queryText, botWrapper);
    }

    async function executeChatFlow(queryText, targetBotWrapper) {
        sendBtn.disabled = true;
        const botMessageElement = targetBotWrapper.querySelector('.message');
        botMessageElement.innerHTML = '<div class="tech-loading"><span></span><span></span><span></span></div>';

        const formData = new FormData();
        formData.append('query', queryText);
        formData.append('language', targetLang.value);
        formData.append('conversation_id', currentConversationId);
        
        if (documentFile.files.length > 0) {
            formData.append('file', documentFile.files[0]);
        }

        try {
            const response = await fetch('/api/chatflow', { method: 'POST', body: formData });
            if (!response.ok) {
                const errData = await response.json();
                throw new Error(errData.error || "HTTP " + response.status);
            }

            const result = await response.json();
            if (result.answer) {
                botMessageElement.innerHTML = result.answer;
                
                if (result.conversation_id && !currentConversationId) {
                    currentConversationId = result.conversation_id;
                    convIdTag.innerText = "CONV_ID: " + currentConversationId;
                    lockFileField();
                }
                // 刷新左侧会话池
                await loadHistoryList();
            } else {
                botMessageElement.innerHTML = "<span style='color: #ef4444;'>[WARNING] PROCESS_COMPLETED_WITHOUT_ANSWER</span>";
            }
        } catch (error) {
            console.error('Fetch Error:', error);
            botMessageElement.innerHTML = "<span style='color: #ef4444;'>SYS_ERR: " + error.message.toUpperCase() + "</span>";
        } finally {
            sendBtn.disabled = false; userInput.focus(); scrollToBottom();
        }
    }

    sendBtn.addEventListener('click', sendMessage);
</script>

</body>
</html>
"""

# ==================== 后端代理路由与持久化控制层 ====================

def upload_to_dify(file_bytes, filename, mime_type):
    url = f"{DIFY_BASE_URL}/v1/files/upload"
    headers = { 'Authorization': f'Bearer {DIFY_API_KEY}' }
    data = { 'user': USER_ID }
    files = { 'file': (filename, file_bytes, mime_type) }
    
    try:
        resp = requests.post(url, headers=headers, data=data, files=files, timeout=30)
        if resp.status_code in (200, 201):
            return resp.json().get('id')
        return None
    except Exception:
        return None

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/history', methods=['GET'])
def get_all_history():
    return jsonify(load_db())

@app.route('/api/history/<conv_id>', methods=['GET'])
def get_one_history(conv_id):
    db = load_db()
    for s in db["sessions"]:
        if s["id"] == conv_id:
            return jsonify(s)
    return jsonify({"id": conv_id, "title": "未知会话", "messages": []})

@app.route('/api/history/<conv_id>', methods=['DELETE'])
def delete_history_item(conv_id):
    db = load_db()
    db["sessions"] = [s for s in db["sessions"] if s["id"] != conv_id]
    save_db(db)
    return jsonify({"status": "success"})

@app.route('/api/chatflow', methods=['POST'])
def chatflow_proxy():
    query = request.form.get('query')
    language = request.form.get('language', '中文')
    conversation_id = request.form.get('conversation_id', '')
    uploaded_file = request.files.get('file')

    file_id = None
    if uploaded_file and not conversation_id:
        file_bytes = uploaded_file.read()
        filename = uploaded_file.filename
        mime_type = uploaded_file.content_type or 'application/octet-stream'
        
        file_id = upload_to_dify(file_bytes, filename, mime_type)
        if not file_id:
            return jsonify({"error": "ATTACHMENT_MOUNT_FAILED"}), 500
    elif conversation_id and uploaded_file:
        return jsonify({"error": "SESSION_LOCKED_CANNOT_ADD_FILE"}), 400

    inputs = {
        "target_language": language,
        "y": "123"
    }
    
    if file_id:
        inputs["upload"] = {
            "type": "document",
            "transfer_method": "local_file",
            "upload_file_id": file_id
        }

    payload = {
        "inputs": inputs,
        "query": query,
        "response_mode": "blocking",
        "conversation_id": conversation_id,
        "user": USER_ID
    }

    url = f"{DIFY_BASE_URL}/v1/chat-messages"
    headers = {
        "Authorization": f"Bearer {DIFY_API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        resp = requests.post(url, headers=headers, json=payload, timeout=60)
        if resp.status_code in (200, 201):
            resp_data = resp.json()
            new_conv_id = resp_data.get('conversation_id')
            ai_answer = resp_data.get('answer')
            
            # 读取本地库，获取已有消息列表或新建
            db = load_db()
            active_messages = []
            target_id = conversation_id if conversation_id else new_conv_id
            
            for s in db["sessions"]:
                if s["id"] == target_id:
                    active_messages = s["messages"]
                    break
            
            # 追加本次交互到本地库中
            active_messages.append({"sender": "user", "content": query})
            active_messages.append({"sender": "bot", "content": ai_answer})
            
            # 更新/持久化本地 JSON
            update_session(target_id, query, active_messages)
            
            return jsonify(resp_data)
        else:
            return jsonify({"error": f"DIFY_GATEWAY_ERROR_{resp.status_code}"}), resp.status_code
    except Exception as e:
        return jsonify({"error": f"LOCAL_PROXY_EXCEPTION_{str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
