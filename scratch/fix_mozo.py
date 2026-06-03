import os

filepath = r"tasks/templates/panel_mozo.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    '<body>': '<body class="restaurant-layout dashboard-body">',
    '<aside class="sidebar">': '<aside class="restaurant-sidebar">',
    'class="nav-item"': 'class="sidebar-link"',
    'class="nav-item active"': 'class="sidebar-link active"',
    'class="new-order-btn"': 'class="sidebar-new-order"',
    '<main class="main-content">': '<main class="restaurant-main">',
    '<header class="top-header">': '<header class="restaurant-topbar">',
    '<div class="header-actions">': '<div class="topbar-actions">',
    '<div class="profile-circle">': '<div class="profile-avatar">',
    '<section class="menu-section">': '<section class="restaurant-menu">',
    '<div class="section-top">': '<div class="menu-header">',
    '<div class="category-filters">': '<div class="menu-filters">',
    '<div class="menu-image">': '<div class="menu-card-image">',
    'class="price-tag"': 'class="menu-price"',
    '<div class="menu-info">': '<div class="menu-card-content">',
    '<aside class="cart-sidebar">': '<aside class="order-sidebar">',
    '<div class="cart-header">': '<div class="order-header">',
    'class="dine-badge"': 'class="order-type"',
    '<div class="table-buttons">': '<div class="table-selector">',
    'class="quantity"': 'class="cart-quantity"',
    '<div class="comment-box">': '<div class="order-comment">',
    '<div class="cart-total">': '<div class="order-summary">',
    '<div class="price-row">': '<div class="summary-row">',
    '<div class="price-row total">': '<div class="summary-row summary-total">',
    'class="send-btn"': 'class="send-kitchen-btn"',
    '<footer class="bottom-footer">': '<footer class="restaurant-footer">',
    '<div class="footer-item">': '<div class="footer-stat">',
    '<div class="footer-icon red">': '<div class="footer-stat-icon red">',
    '<div class="footer-icon yellow">': '<div class="footer-stat-icon yellow">',
}

for old, new in replacements.items():
    content = content.replace(old, new)

# specific button replacements in topbar
content = content.replace('<button>\n\n                    <span class="material-symbols-outlined">\n                        notifications', '<button class="topbar-icon">\n\n                    <span class="material-symbols-outlined">\n                        notifications')
content = content.replace('<button>\n\n                    <span class="material-symbols-outlined">\n                        local_fire_department', '<button class="topbar-icon">\n\n                    <span class="material-symbols-outlined">\n                        local_fire_department')

# specific button replacements in menu-filters
content = content.replace('<button class="active">\n                            All\n                        </button>', '<button class="filter-btn active">\n                            All\n                        </button>')
content = content.replace('<button>\n                            Burgers\n                        </button>', '<button class="filter-btn">\n                            Burgers\n                        </button>')
content = content.replace('<button>\n                            Sides\n                        </button>', '<button class="filter-btn">\n                            Sides\n                        </button>')
content = content.replace('<button>\n                            Drinks\n                        </button>', '<button class="filter-btn">\n                            Drinks\n                        </button>')

# specific button replacements in table-selector
content = content.replace('<button class="active">\n                            Table 12\n                        </button>', '<button class="table-btn active">\n                            Table 12\n                        </button>')
content = content.replace('<button>\n                            Table 14\n                        </button>', '<button class="table-btn">\n                            Table 14\n                        </button>')
content = content.replace('<button>\n                            Guest 3\n                        </button>', '<button class="table-btn">\n                            Guest 3\n                        </button>')

# fix cart prices
content = content.replace('<strong>\n                            $12.99\n                        </strong>', '<strong class="cart-price">\n                            $12.99\n                        </strong>')
content = content.replace('<strong>\n                            $9.00\n                        </strong>', '<strong class="cart-price">\n                            $9.00\n                        </strong>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated panel_mozo.html")
