#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

# unblockgw 目录路径
DIR_PATH = os.path.dirname(os.path.realpath(__file__))

# Unblock Youku 的规则文件 urls.js 链接
UNBLOCK_YOUKU_URLSJS_URL = "https://raw.githubusercontent.com/uku/Unblock-Youku/master/shared/urls.js"

# --- router ---

# python3 命令路径
PYTHON3_PATH = "/usr/bin/python3"

# TPROXY 本地端口
PROXY_LOCAL_PORT = 1080

# iptables 添加 chn ipset 规则命令
ADD_IPTABLES_CHN_CMD = "iptables -t nat -A PREROUTING -p tcp -m set --match-set chn dst -j REDIRECT --to-port {}".format(PROXY_LOCAL_PORT)
# iptables 删除 chn ipset 规则命令
DELETE_IPTABLES_CHN_CMD = "iptables -t nat -D PREROUTING -p tcp -m set --match-set chn dst -j REDIRECT --to-port {}".format(PROXY_LOCAL_PORT)
# iptables 检查 chn ipset 规则命令
CHECK_IPTABLES_CHN_CMD = "iptables -t nat -C PREROUTING -p tcp -m set --match-set chn dst -j REDIRECT --to-port {}".format(PROXY_LOCAL_PORT)

# ipset 规则配置文件的保存路径
IPSET_CONF_PATH = "configs/ipset.rules"

# services-start 启动脚本路径
SERVICES_START_SCRIPT_PATH = "scripts/services-start"
# nat-start 启动脚本路径
NAT_START_SCRIPT_PATH = "scripts/nat-start"

# 定时每天几点更新规则
RENEW_TIME = 3


