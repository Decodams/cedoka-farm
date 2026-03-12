import re

files = ['index.html', 'about.html', 'shop.html', 'contact.html', 'productdetail.html']

mobile_nav_template = """    <!-- Mobile Navigation -->
    <div id="mobile-nav"
        class="fixed inset-0 z-[100] bg-white/95 backdrop-blur-md transform translate-x-full transition-transform duration-300 flex flex-col pt-24 px-6 md:px-10 pb-10 overflow-y-auto lg:hidden">
        <button onclick="toggleMobileNav()"
            class="absolute top-6 right-6 text-primary hover:text-gold transition-colors">
            <span class="material-symbols-outlined text-4xl">close</span>
        </button>
        <nav class="flex flex-col gap-6 items-center">
            <a class="{HM_MOB} text-2xl uppercase tracking-widest hover:text-gold transition-colors" href="index.html">Home</a>
            <a class="{AB_MOB} text-2xl uppercase tracking-widest hover:text-gold transition-colors" href="about.html">About</a>
            <a class="{SH_MOB} text-2xl uppercase tracking-widest hover:text-gold transition-colors" href="shop.html">Shop</a>
            <a class="{CO_MOB} text-2xl uppercase tracking-widest hover:text-gold transition-colors" href="contact.html">Contact</a>
        </nav>
        <div class="mt-auto pt-10 text-center text-primary/70 flex flex-col items-center gap-2">
            <span class="material-symbols-outlined text-gold">location_on</span>
            <p class="font-bold">Awka, Nigeria</p>
        </div>
    </div>"""

header_template = """    <!-- Sticky Navbar -->
    <header class="sticky top-0 z-50 w-full border-b border-primary/10 bg-white/95 backdrop-blur-md px-6 md:px-10 lg:px-20 py-4">
        <div class="mx-auto flex max-w-7xl items-center justify-between gap-8">
            <a href="index.html" class="flex items-center gap-2 z-50 relative shrink-0">
                <img src="assets/logo.png" alt="Cedoka Farms" class="h-10 md:h-12 w-auto object-contain" />
            </a>
            <nav class="hidden lg:flex items-center gap-10">
                <a class="{HM_DESK} text-sm uppercase tracking-widest hover:text-gold transition-colors" href="index.html">Home</a>
                <a class="{AB_DESK} text-sm uppercase tracking-widest hover:text-gold transition-colors" href="about.html">About</a>
                <a class="{SH_DESK} text-sm uppercase tracking-widest hover:text-gold transition-colors" href="shop.html">Shop</a>
                <a class="{CO_DESK} text-sm uppercase tracking-widest hover:text-gold transition-colors" href="contact.html">Contact</a>
            </nav>
            <div class="flex items-center gap-4">
                <a href="shop.html"
                    class="{BTN_CLS}">
                    SHOP NOW
                </a>
                <button onclick="toggleMobileNav()"
                    class="lg:hidden ml-4 text-primary hover:text-gold transition-colors z-50 flex items-center justify-center">
                    <span class="material-symbols-outlined text-3xl">menu</span>
                </button>
            </div>
        </div>
    </header>"""

footer_template = """    <!-- Premium Footer -->
    <footer class="mt-20 border-t border-primary/10 bg-white dark:bg-slate-900 py-16">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12">
                <div class="space-y-6">
                    <img src="assets/logo.png" alt="Cedoka Farms" class="h-10 w-auto object-contain" />
                    <div class="flex gap-2 items-center text-primary mt-2">
                        <span class="material-symbols-outlined">location_on</span>
                        <p class="text-sm font-bold">Awka, Nigeria</p>
                    </div>
                    <p class="text-sm text-slate-500 dark:text-slate-400 leading-relaxed font-medium">Cultivating a sustainable future through organic farming and ethical practices.</p>
                </div>
                <div>
                    <h4 class="font-black text-primary mb-6 uppercase tracking-wider">Quick Links</h4>
                    <ul class="space-y-4 text-sm font-medium text-slate-500 dark:text-slate-400">
                        <li><a class="hover:text-gold transition" href="#">Organic Certification</a></li>
                        <li><a class="hover:text-gold transition" href="#">About Our Process</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="font-black text-primary mb-6 uppercase tracking-wider">Customer Care</h4>
                    <ul class="space-y-4 text-sm font-medium text-slate-500 dark:text-slate-400">
                        <li><a class="hover:text-gold transition" href="#">Help Center & FAQ</a></li>
                        <li><a class="hover:text-gold transition" href="#">Refund Policy</a></li>
                    </ul>
                </div>
            </div>
            <div class="mt-16 pt-8 border-t border-primary/10 text-center">
                <p class="text-sm text-slate-500 font-bold tracking-wide">&copy; 2026 Cedoka Farms. All rights reserved.</p>
            </div>
        </div>
    </footer>"""

mob_nav_regex = re.compile(r'<!-- Mobile Navigation -->.*?</div>\s*(?=<!-- Sticky Navbar -->|<header)', re.DOTALL)
header_regex = re.compile(r'<header[^>]*>.*?</header>', re.DOTALL)
footer_regex = re.compile(r'<footer[^>]*>.*?</footer>', re.DOTALL)

for f in files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            
        print(f"Modifying {f}...")
        
        # Configure active states based on filename
        hm_mob = "text-primary font-black" if f == "index.html" else "text-primary/70 font-bold"
        ab_mob = "text-primary font-black" if f == "about.html" else "text-primary/70 font-bold"
        sh_mob = "text-primary font-black" if f == "shop.html" else "text-primary/70 font-bold"
        co_mob = "text-primary font-black" if f == "contact.html" else "text-primary/70 font-bold"
        
        hm_desk = "text-primary font-black" if f == "index.html" else "text-primary/70 font-bold"
        ab_desk = "text-primary font-black" if f == "about.html" else "text-primary/70 font-bold"
        sh_desk = "text-primary font-black" if f == "shop.html" else "text-primary/70 font-bold"
        co_desk = "text-primary font-black" if f == "contact.html" else "text-primary/70 font-bold"
        
        btn_cls = "hidden sm:inline-block bg-primary text-white px-6 py-2.5 rounded-none text-xs font-bold tracking-widest hover:bg-gold transition-all outline-none"
        if f == "shop.html":
            btn_cls = "hidden sm:inline-block bg-gold text-primary px-6 py-2.5 rounded-none text-xs font-black tracking-widest hover:bg-gold/90 transition-all outline-none"

        new_mob = mobile_nav_template.format(HM_MOB=hm_mob, AB_MOB=ab_mob, SH_MOB=sh_mob, CO_MOB=co_mob)
        new_desk = header_template.format(HM_DESK=hm_desk, AB_DESK=ab_desk, SH_DESK=sh_desk, CO_DESK=co_desk, BTN_CLS=btn_cls)
        
        content = mob_nav_regex.sub(new_mob + "\n\n", content)
        content = header_regex.sub(new_desk, content)
        content = footer_regex.sub(footer_template, content)
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
            
        print(f"Saved {f} successfully.")
    except Exception as e:
        print(f"Error processing {f}: {e}")
