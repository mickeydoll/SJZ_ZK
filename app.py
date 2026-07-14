import streamlit as st
import math
from typing import List, Dict

# ----------------------------- 页面配置 -----------------------------
st.set_page_config(
    page_title="石家庄中考志愿推荐 2026-2027",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ----------------------------- 学校数据库 -----------------------------
# 分数线基于650分满分体系（近年数据 + 2026-2027预测）
SCHOOLS: List[Dict] = [
    {
        "id": 1,
        "name": "石家庄二中（本部）",
        "subtitle": "河北省重点 · 省级示范性高中",
        "region": "市区",
        "district": "新华区",
        "type": "公办",
        "category": "省级示范性高中",
        "batch": 1,
        "score_predicted": 634,
        "score_range": [628, 640],
        "features": ["理科顶尖", "竞赛强校", "清北录取率高", "师资雄厚"],
        "boarding": "可寄宿",
        "address": "新华区兴凯路187号",
        "key_school": True,
        "rank": 1
    },
    {
        "id": 2,
        "name": "石家庄一中（本部）",
        "subtitle": "河北省重点 · 省级示范性高中",
        "region": "市区",
        "district": "长安区",
        "type": "公办",
        "category": "省级示范性高中",
        "batch": 1,
        "score_predicted": 624,
        "score_range": [618, 630],
        "features": ["文理均衡", "历史悠久", "学风严谨", "985录取率高"],
        "boarding": "可寄宿",
        "address": "长安区中山东路",
        "key_school": True,
        "rank": 2
    },
    {
        "id": 3,
        "name": "石家庄二中实验学校（二中南校区）",
        "subtitle": "省级示范性高中 · 二中教育集团",
        "region": "市区",
        "district": "裕华区",
        "type": "公办",
        "category": "省级示范性高中",
        "batch": 1,
        "score_predicted": 617,
        "score_range": [610, 625],
        "features": ["理科强校", "集团化办学", "资源丰富", "竞赛成绩好"],
        "boarding": "可寄宿",
        "address": "裕华区",
        "key_school": True,
        "rank": 3
    },
    {
        "id": 4,
        "name": "河北正定中学",
        "subtitle": "河北省重点 · 百年名校",
        "region": "正定",
        "district": "正定县",
        "type": "公办",
        "category": "省级示范性高中",
        "batch": 1,
        "score_predicted": 610,
        "score_range": [603, 618],
        "features": ["百年历史", "文理兼备", "校园优美", "文化底蕴深"],
        "boarding": "寄宿制",
        "address": "正定县府西街",
        "key_school": True,
        "rank": 4
    },
    {
        "id": 5,
        "name": "石家庄精英中学",
        "subtitle": "民办名校 · 省级示范性高中",
        "region": "市区",
        "district": "裕华区",
        "type": "民办",
        "category": "省级示范性高中（民办）",
        "batch": 1,
        "score_predicted": 607,
        "score_range": [598, 616],
        "features": ["管理严格", "升学率高", "全封闭管理", "小班教学"],
        "boarding": "全寄宿",
        "address": "裕华区学苑路",
        "key_school": True,
        "rank": 5
    },
    {
        "id": 6,
        "name": "石家庄外国语学校（43中）",
        "subtitle": "省级示范性高中 · 外语特色",
        "region": "市区",
        "district": "裕华区",
        "type": "公办",
        "category": "省级示范性高中",
        "batch": 1,
        "score_predicted": 600,
        "score_range": [592, 608],
        "features": ["外语特色", "国际部", "文科较强", "保送机会"],
        "boarding": "可寄宿",
        "address": "裕华区育才街",
        "key_school": True,
        "rank": 6
    },
    {
        "id": 7,
        "name": "石家庄二十四中",
        "subtitle": "省级示范性高中",
        "region": "市区",
        "district": "桥西区",
        "type": "公办",
        "category": "省级示范性高中",
        "batch": 1,
        "score_predicted": 594,
        "score_range": [585, 602],
        "features": ["文科优势", "艺术特色", "社团丰富", "地理位置好"],
        "boarding": "部分寄宿",
        "address": "桥西区自强路",
        "key_school": True,
        "rank": 7
    },
    {
        "id": 8,
        "name": "辛集中学",
        "subtitle": "河北省重点 · 省级示范性高中",
        "region": "辛集",
        "district": "辛集市",
        "type": "公办",
        "category": "省级示范性高中",
        "batch": 1,
        "score_predicted": 590,
        "score_range": [580, 598],
        "features": ["县中典范", "理科较强", "升学稳定", "校风朴实"],
        "boarding": "寄宿制",
        "address": "辛集市",
        "key_school": True,
        "rank": 8
    },
    {
        "id": 9,
        "name": "石家庄实验中学",
        "subtitle": "省级示范性高中",
        "region": "市区",
        "district": "新华区",
        "type": "公办",
        "category": "省级示范性高中",
        "batch": 1,
        "score_predicted": 582,
        "score_range": [572, 590],
        "features": ["实验班突出", "理科教学好", "管理规范"],
        "boarding": "可寄宿",
        "address": "新华区",
        "key_school": True,
        "rank": 9
    },
    {
        "id": 10,
        "name": "石家庄一中东校区",
        "subtitle": "省级示范性高中 · 一中教育集团",
        "region": "市区",
        "district": "长安区",
        "type": "公办",
        "category": "省级示范性高中",
        "batch": 1,
        "score_predicted": 577,
        "score_range": [568, 586],
        "features": ["集团资源", "新校区设施好", "发展迅速"],
        "boarding": "可寄宿",
        "address": "长安区",
        "key_school": True,
        "rank": 10
    },
    {
        "id": 11,
        "name": "石家庄四十二中",
        "subtitle": "省级示范性高中",
        "region": "市区",
        "district": "新华区",
        "type": "公办",
        "category": "省级示范性高中",
        "batch": 1,
        "score_predicted": 570,
        "score_range": [560, 578],
        "features": ["稳步提升", "综合发展", "师资稳定"],
        "boarding": "部分寄宿",
        "address": "新华区",
        "key_school": True,
        "rank": 11
    },
    {
        "id": 12,
        "name": "石家庄十七中",
        "subtitle": "省级示范性高中",
        "region": "市区",
        "district": "桥西区",
        "type": "公办",
        "category": "省级示范性高中",
        "batch": 1,
        "score_predicted": 564,
        "score_range": [554, 572],
        "features": ["文科较好", "地理位置佳", "走读方便"],
        "boarding": "走读为主",
        "address": "桥西区",
        "key_school": True,
        "rank": 12
    },
    {
        "id": 13,
        "name": "石家庄师大附中",
        "subtitle": "省级示范性高中 · 高校附属",
        "region": "市区",
        "district": "长安区",
        "type": "公办",
        "category": "省级示范性高中",
        "batch": 1,
        "score_predicted": 560,
        "score_range": [550, 568],
        "features": ["高校资源", "教师培训好", "学术氛围"],
        "boarding": "可寄宿",
        "address": "长安区",
        "key_school": True,
        "rank": 13
    },
    {
        "id": 14,
        "name": "石家庄十五中",
        "subtitle": "省级示范性高中",
        "region": "市区",
        "district": "裕华区",
        "type": "公办",
        "category": "省级示范性高中",
        "batch": 1,
        "score_predicted": 554,
        "score_range": [544, 562],
        "features": ["稳步发展", "综合培养", "社区关系好"],
        "boarding": "走读为主",
        "address": "裕华区",
        "key_school": True,
        "rank": 14
    },
    {
        "id": 15,
        "name": "石家庄九中",
        "subtitle": "省级示范性高中",
        "region": "市区",
        "district": "新华区",
        "type": "公办",
        "category": "省级示范性高中",
        "batch": 2,
        "score_predicted": 547,
        "score_range": [536, 556],
        "features": ["中等偏上", "稳定可靠", "适合中等生"],
        "boarding": "部分寄宿",
        "address": "新华区",
        "key_school": False,
        "rank": 15
    },
    {
        "id": 16,
        "name": "石家庄二十七中",
        "subtitle": "市级示范性高中",
        "region": "市区",
        "district": "裕华区",
        "type": "公办",
        "category": "市级示范性高中",
        "batch": 2,
        "score_predicted": 537,
        "score_range": [526, 546],
        "features": ["中等层次", "艺术有特色", "社区学校"],
        "boarding": "走读为主",
        "address": "裕华区",
        "key_school": False,
        "rank": 16
    },
    {
        "id": 17,
        "name": "石家庄二十三中",
        "subtitle": "市级示范性高中",
        "region": "市区",
        "district": "长安区",
        "type": "公办",
        "category": "市级示范性高中",
        "batch": 2,
        "score_predicted": 527,
        "score_range": [516, 536],
        "features": ["中等层次", "交通便利", "适合走读"],
        "boarding": "走读",
        "address": "长安区",
        "key_school": False,
        "rank": 17
    },
    {
        "id": 18,
        "name": "石家庄四十一中",
        "subtitle": "市级示范性高中",
        "region": "市区",
        "district": "桥西区",
        "type": "公办",
        "category": "市级示范性高中",
        "batch": 2,
        "score_predicted": 522,
        "score_range": [510, 532],
        "features": ["市区便利", "中等水平", "稳定"],
        "boarding": "走读",
        "address": "桥西区",
        "key_school": False,
        "rank": 18
    },
    {
        "id": 19,
        "name": "石家庄二十八中",
        "subtitle": "市级示范性高中",
        "region": "市区",
        "district": "新华区",
        "type": "公办",
        "category": "市级示范性高中",
        "batch": 2,
        "score_predicted": 517,
        "score_range": [505, 526],
        "features": ["中等偏下", "适合基础较弱学生"],
        "boarding": "走读",
        "address": "新华区",
        "key_school": False,
        "rank": 19
    },
    {
        "id": 20,
        "name": "石家庄二十二中",
        "subtitle": "普通高中",
        "region": "市区",
        "district": "长安区",
        "type": "公办",
        "category": "普通高中",
        "batch": 3,
        "score_predicted": 502,
        "score_range": [490, 512],
        "features": ["普通高中", "基础培养"],
        "boarding": "走读",
        "address": "长安区",
        "key_school": False,
        "rank": 20
    },
    {
        "id": 21,
        "name": "石家庄四中",
        "subtitle": "普通高中",
        "region": "市区",
        "district": "桥西区",
        "type": "公办",
        "category": "普通高中",
        "batch": 3,
        "score_predicted": 497,
        "score_range": [485, 506],
        "features": ["市区普高", "地理位置好"],
        "boarding": "走读",
        "address": "桥西区",
        "key_school": False,
        "rank": 21
    },
    {
        "id": 22,
        "name": "石家庄十八中",
        "subtitle": "普通高中",
        "region": "市区",
        "district": "新华区",
        "type": "公办",
        "category": "普通高中",
        "batch": 3,
        "score_predicted": 490,
        "score_range": [478, 500],
        "features": ["普通高中", "艺术班可选"],
        "boarding": "走读",
        "address": "新华区",
        "key_school": False,
        "rank": 22
    },
    {
        "id": 23,
        "name": "石家庄十中",
        "subtitle": "普通高中",
        "region": "市区",
        "district": "桥西区",
        "type": "公办",
        "category": "普通高中",
        "batch": 3,
        "score_predicted": 482,
        "score_range": [470, 492],
        "features": ["普高线附近", "基础教学"],
        "boarding": "走读",
        "address": "桥西区",
        "key_school": False,
        "rank": 23
    },
    {
        "id": 24,
        "name": "石家庄六中",
        "subtitle": "普通高中 · 艺术特色",
        "region": "市区",
        "district": "桥西区",
        "type": "公办",
        "category": "普通高中",
        "batch": 3,
        "score_predicted": 474,
        "score_range": [460, 484],
        "features": ["艺术特色", "美术班", "音乐班"],
        "boarding": "走读",
        "address": "桥西区",
        "key_school": False,
        "rank": 24
    },
    {
        "id": 25,
        "name": "石家庄润德学校（二中润德）",
        "subtitle": "民办高中 · 二中教育集团",
        "region": "市区",
        "district": "裕华区",
        "type": "民办",
        "category": "民办高中",
        "batch": 3,
        "score_predicted": 557,
        "score_range": [545, 568],
        "features": ["二中品牌", "民办灵活", "小班化"],
        "boarding": "全寄宿",
        "address": "裕华区",
        "key_school": False,
        "rank": 25
    },
    {
        "id": 26,
        "name": "石家庄卓越中学",
        "subtitle": "民办高中",
        "region": "市区",
        "district": "长安区",
        "type": "民办",
        "category": "民办高中",
        "batch": 3,
        "score_predicted": 533,
        "score_range": [520, 545],
        "features": ["民办新秀", "管理较严", "小班教学"],
        "boarding": "全寄宿",
        "address": "长安区",
        "key_school": False,
        "rank": 26
    },
    {
        "id": 27,
        "name": "石家庄金石中学",
        "subtitle": "民办高中",
        "region": "市区",
        "district": "裕华区",
        "type": "民办",
        "category": "民办高中",
        "batch": 3,
        "score_predicted": 508,
        "score_range": [495, 520],
        "features": ["民办", "中等层次", "寄宿制"],
        "boarding": "全寄宿",
        "address": "裕华区",
        "key_school": False,
        "rank": 27
    },
    {
        "id": 28,
        "name": "石家庄联邦国际学校",
        "subtitle": "民办高中 · 国际课程",
        "region": "市区",
        "district": "裕华区",
        "type": "民办",
        "category": "民办高中",
        "batch": 3,
        "score_predicted": 493,
        "score_range": [478, 508],
        "features": ["国际课程", "出国方向", "英语强化"],
        "boarding": "全寄宿",
        "address": "裕华区",
        "key_school": False,
        "rank": 28
    },
    {
        "id": 29,
        "name": "石家庄第二实验中学",
        "subtitle": "省级示范性高中",
        "region": "市区",
        "district": "新华区",
        "type": "公办",
        "category": "省级示范性高中",
        "batch": 1,
        "score_predicted": 572,
        "score_range": [562, 580],
        "features": ["实验班", "教学扎实", "上升期"],
        "boarding": "可寄宿",
        "address": "新华区",
        "key_school": True,
        "rank": 29
    },
    {
        "id": 30,
        "name": "石家庄西山学校",
        "subtitle": "民办高中",
        "region": "鹿泉",
        "district": "鹿泉区",
        "type": "民办",
        "category": "民办高中",
        "batch": 3,
        "score_predicted": 478,
        "score_range": [465, 490],
        "features": ["环境优美", "寄宿制", "鹿泉区"],
        "boarding": "全寄宿",
        "address": "鹿泉区",
        "key_school": False,
        "rank": 30
    },
    {
        "id": 31,
        "name": "栾城中学",
        "subtitle": "区属重点高中",
        "region": "栾城",
        "district": "栾城区",
        "type": "公办",
        "category": "区属示范性高中",
        "batch": 2,
        "score_predicted": 512,
        "score_range": [500, 522],
        "features": ["区属重点", "本地生源为主"],
        "boarding": "可寄宿",
        "address": "栾城区",
        "key_school": False,
        "rank": 31
    },
    {
        "id": 32,
        "name": "藁城一中",
        "subtitle": "区属重点高中",
        "region": "藁城",
        "district": "藁城区",
        "type": "公办",
        "category": "区属示范性高中",
        "batch": 2,
        "score_predicted": 510,
        "score_range": [498, 520],
        "features": ["区属重点", "藁城区最佳"],
        "boarding": "可寄宿",
        "address": "藁城区",
        "key_school": False,
        "rank": 32
    },
    {
        "id": 33,
        "name": "鹿泉一中",
        "subtitle": "区属重点高中",
        "region": "鹿泉",
        "district": "鹿泉区",
        "type": "公办",
        "category": "区属示范性高中",
        "batch": 2,
        "score_predicted": 507,
        "score_range": [495, 518],
        "features": ["区属重点", "鹿泉区", "环境好"],
        "boarding": "可寄宿",
        "address": "鹿泉区",
        "key_school": False,
        "rank": 33
    }
]

# ----------------------------- 辅助函数 -----------------------------
def classify_schools(schools: List[Dict], user_score_normalized: float) -> List[Dict]:
    """
    根据标准化分数（满分650）将学校分为冲刺、稳妥、保底三类。
    返回添加了 'match_type' 和 'gap' 字段的学校列表。
    """
    result = []
    for s in schools:
        line = s["score_predicted"]
        gap = user_score_normalized - line
        if gap >= 10:
            match_type = "guarantee"   # 保底
        elif gap >= -5:
            match_type = "safe"        # 稳妥
        elif gap >= -20:
            match_type = "sprint"      # 冲刺
        else:
            match_type = "out_of_reach" # 差距过大
        result.append({**s, "gap": round(gap), "match_type": match_type})
    return result

def get_wishlist_from_state():
    """从 session_state 中获取志愿表集合（Set of school ids）"""
    if "wishlist" not in st.session_state:
        st.session_state.wishlist = set()
    return st.session_state.wishlist

def toggle_wishlist(school_id: int):
    """切换某个学校的收藏状态"""
    wishlist = get_wishlist_from_state()
    if school_id in wishlist:
        wishlist.discard(school_id)
    else:
        wishlist.add(school_id)

# ----------------------------- 界面渲染 -----------------------------
def main():
    st.title("🎓 石家庄中考志愿推荐系统 (2026‑2027)")
    st.markdown("**数据参考近年录取线，结合2026-2027年预测。总分可自定义，默认满分650分。**")
    st.markdown("---")

    # ---------- 侧边栏：参数设置 ----------
    with st.sidebar:
        st.header("⚙️ 参数设置")
        user_score = st.number_input(
            "你的预估中考分数",
            min_value=200,
            max_value=750,
            value=580,
            step=1,
            help="输入你的中考预估总分（含体育、实验等）"
        )

        # 在侧边栏增加考生信息
        with st.sidebar:
            st.header("👤 考生信息")
            candidate_name = st.text_input("姓名", placeholder="请输入考生姓名")
            candidate_gender = st.radio("性别", ["男", "女"], horizontal=True)
            candidate_school = st.text_input("毕业初中", placeholder="请输入初中学校")
            is_indicator = st.checkbox("是否享受指标生（分配生）政策")

        total_score = st.number_input(
            "中考满分设置",
            min_value=400,
            max_value=800,
            value=650,
            step=10,
            help="根据当地政策调整满分值"
        )
        region_filter = st.selectbox(
            "区域筛选",
            options=["全部区域", "市区", "正定", "辛集", "栾城", "藁城", "鹿泉", "其他"],
            index=0
        )
        st.markdown("---")
        st.caption("💡 选择区域后仅显示对应区县的学校")

    # 计算标准化分数（统一换算到650分基准）
    if total_score > 0:
        normalized_score = (user_score / total_score) * 650
    else:
        normalized_score = 0

    # 显示得分率
    score_pct = (user_score / total_score * 100) if total_score > 0 else 0
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("你的分数", f"{user_score} 分", f"得分率 {score_pct:.1f}%")
    with col2:
        st.metric("满分设置", f"{total_score} 分")
    with col3:
        st.metric("换算650分基准", f"{normalized_score:.1f} 分")

    # 区域筛选逻辑
    region_key = region_filter.replace("全部区域", "all")
    if region_key == "all":
        filtered_schools = SCHOOLS.copy()
    else:
        filtered_schools = [s for s in SCHOOLS if s["region"] == region_key]

    # 分类计算
    classified = classify_schools(filtered_schools, normalized_score)

    # 提取三个梯度（排除差距过大的学校）
    sprint_schools = [s for s in classified if s["match_type"] == "sprint"]
    safe_schools   = [s for s in classified if s["match_type"] == "safe"]
    guarantee_schools = [s for s in classified if s["match_type"] == "guarantee"]
    out_of_reach = [s for s in classified if s["match_type"] == "out_of_reach"]

    # 按分数排序（冲刺：从高到低，稳妥：从低到高，保底：从高到低）
    sprint_schools.sort(key=lambda x: x["gap"], reverse=True)   # 差距大的在前（更冲刺）
    safe_schools.sort(key=lambda x: x["gap"])                   # 差距小的更稳妥
    guarantee_schools.sort(key=lambda x: x["gap"], reverse=True) # 高出分数多的在前

    # 合并显示列表
    display_schools = sprint_schools + safe_schools + guarantee_schools

    # ---------- 统计概览 ----------
    st.markdown("### 📊 匹配概览")
    cols = st.columns(4)
    cols[0].metric("🔴 冲刺", len(sprint_schools))
    cols[1].metric("🟢 稳妥", len(safe_schools))
    cols[2].metric("🔵 保底", len(guarantee_schools))
    cols[3].metric("📋 总匹配", len(display_schools))
    if out_of_reach:
        st.caption(f"另有 {len(out_of_reach)} 所学校差距较大（低于冲刺线-20分），未在列表中显示。")

    st.markdown("---")

    # ---------- 学校卡片列表 ----------
    st.markdown("## 🏫 推荐学校")
    if not display_schools:
        st.info("没有匹配的学校，请调整分数或区域筛选条件。")
    else:
        # 使用列布局展示卡片（每行3个）
        cols_per_row = 3
        for i in range(0, len(display_schools), cols_per_row):
            row_schools = display_schools[i:i+cols_per_row]
            columns = st.columns(cols_per_row)
            for col, school in zip(columns, row_schools):
                with col:
                    # 卡片样式
                    with st.container(border=True):
                        # 顶部梯度标签
                        match = school["match_type"]
                        if match == "sprint":
                            st.markdown("🔴 **冲刺**  |  差距较大")
                            st.caption(f"需努力！分数差 {abs(school['gap'])} 分")
                        elif match == "safe":
                            st.markdown("🟢 **稳妥**  |  匹配较好")
                            if school["gap"] >= 0:
                                st.caption(f"高出线 {school['gap']} 分")
                            else:
                                st.caption(f"仅差 {abs(school['gap'])} 分")
                        else:  # guarantee
                            st.markdown("🔵 **保底**  |  高概率录取")
                            st.caption(f"高出线 {school['gap']} 分以上")

                        # 学校名称与副标题
                        st.subheader(school["name"])
                        st.markdown(f"*{school['subtitle']}*")

                        # 基本信息
                        st.markdown(f"**类型**：{school['type']} | **区域**：{school['region']} | **寄宿**：{school['boarding']}")
                        if school["key_school"]:
                            st.markdown("⭐ 重点高中")

                        # 分数线（按用户设置的满分换算）
                        displayed_line = round((school["score_predicted"] / 650) * total_score)
                        st.markdown(f"**预估录取线**：`{displayed_line} 分`（满分{total_score}）")

                        # 特色标签
                        features_str = " ".join([f"`{f}`" for f in school["features"]])
                        st.markdown(f"🏷️ {features_str}")

                        # 收藏按钮
                        wishlist = get_wishlist_from_state()
                        is_fav = school["id"] in wishlist
                        btn_label = "❤️ 取消收藏" if is_fav else "🤍 加入志愿表"
                        if st.button(btn_label, key=f"fav_{school['id']}", use_container_width=True):
                            toggle_wishlist(school["id"])
                            st.rerun()

    st.markdown("---")

    # ---------- 我的志愿表 ----------
    st.markdown("## 📝 我的志愿表")
    wishlist = get_wishlist_from_state()
    if not wishlist:
        st.info("还没有收藏学校。点击卡片上的按钮将学校加入志愿表。")
    else:

            st.markdown("## 📝 我的志愿表")
    wishlist = get_wishlist_from_state()
    if not wishlist:
        st.info("还没有收藏学校。点击卡片上的按钮将学校加入志愿表。")
    else:
        # ---------- 新增：显示考生信息 ----------
        if candidate_name or candidate_school:
            info_cols = st.columns(3)
            info_cols[0].markdown(f"**姓名**：{candidate_name or '（未填写）'}")
            info_cols[1].markdown(f"**性别**：{candidate_gender}")
            info_cols[2].markdown(f"**初中**：{candidate_school or '（未填写）'}")
            if is_indicator:
                st.info("✅ 已标记为 **指标生**，填报时请核对目标高中在本校的分配名额。")
            st.markdown("---")
        # ----------------------------------------

        wishlist_schools = [s for s in SCHOOLS if s["id"] in wishlist]
        wishlist_schools.sort(key=lambda x: x["score_predicted"], reverse=True)

        table_data = []
        for idx, s in enumerate(wishlist_schools, 1):
            displayed_line = round((s["score_predicted"] / 650) * total_score)
            table_data.append({
                "序号": idx,
                "学校": s["name"],
                "类型": s["type"],
                "区域": s["region"],
                "预估录取线": f"{displayed_line} 分",
            })
        st.table(table_data)

        wishlist_schools = [s for s in SCHOOLS if s["id"] in wishlist]
        # 按预估录取线降序排列
        wishlist_schools.sort(key=lambda x: x["score_predicted"], reverse=True)

        # 表格显示
        table_data = []
        for idx, s in enumerate(wishlist_schools, 1):
            displayed_line = round((s["score_predicted"] / 650) * total_score)
            table_data.append({
                "序号": idx,
                "学校": s["name"],
                "类型": s["type"],
                "区域": s["region"],
                "预估录取线": f"{displayed_line} 分",
                "操作": f"移除"  # 仅作占位，实际操作通过下方按钮
            })

        st.table(table_data)

        # 批量移除操作
        col1, col2 = st.columns([1, 3])
        with col1:
            if st.button("🗑️ 清空志愿表", type="secondary"):
                st.session_state.wishlist.clear()
                st.rerun()
        with col2:
            st.caption("💡 点击下方学校名称旁的按钮可单独移除")

        # 单独移除按钮
        for s in wishlist_schools:
            if st.button(f"✕ 移除 {s['name']}", key=f"remove_{s['id']}"):
                st.session_state.wishlist.discard(s["id"])
                st.rerun()

    st.markdown("---")
    st.warning("⚠️ 重要提示：本系统数据基于近年录取情况预测，仅供参考。实际录取受当年试题难度、招生计划、报考人数等因素影响。请结合学校官方招生简章及教师建议综合判断。")

if __name__ == "__main__":
    main()