import re

def main():
    header_html = """    <header class="sticky top-0 z-50 w-full border-b border-primary/10 bg-linen/95 backdrop-blur-md px-6 md:px-10 lg:px-20 py-4">
        <div class="mx-auto flex max-w-7xl items-center justify-between gap-8">
            <a href="index.html" class="flex items-center gap-2 z-50 relative shrink-0">
                <img src="assets/logo.png" alt="Cedoka Farms" class="h-10 md:h-12 w-auto object-contain" />
            </a>
            <nav class="hidden lg:flex items-center gap-10">
                <a class="text-primary text-sm font-bold uppercase tracking-widest hover:text-gold transition-colors" href="index.html">Home</a>
                <a class="text-primary/70 text-sm font-bold uppercase tracking-widest hover:text-gold transition-colors" href="about.html">About</a>
                <a class="text-primary/70 text-sm font-bold uppercase tracking-widest hover:text-gold transition-colors" href="shop.html">Shop</a>
                <a class="text-primary/70 text-sm font-bold uppercase tracking-widest hover:text-gold transition-colors" href="contact.html">Contact</a>
            </nav>
            <div class="flex items-center gap-4">
                <a href="shop.html" class="hidden sm:inline-block bg-primary text-white px-6 py-2.5 rounded-none text-xs font-bold tracking-widest hover:bg-primary/95 transition-all outline-none">
                    SHOP NOW
                </a>
                <button onclick="toggleMobileNav()" class="lg:hidden ml-4 text-primary hover:text-gold transition-colors z-50 flex items-center justify-center">
                    <span class="material-symbols-outlined text-3xl">menu</span>
                </button>
            </div>
        </div>
    </header>"""

    files = ['index.html', 'about.html', 'shop.html']
    
    for filename in files:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Regular expression to match any <header>...</header> tags including their content
        header_regex = re.compile(r'<header[^>]*>.*?</header>', re.DOTALL)
        
        # In shop.html, there's "<!-- Sticky Navbar -->\n" before the header, let's just let regex replace the <header> block.
        if header_regex.search(content):
            new_content = header_regex.sub(header_html, content)
            
            # Since index.html had the "Cedoka Farms" commented out in footer but wait,
            # this only replaces the <header> element!
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
                print(f"Updated {filename}")
        else:
            print(f"Header not found in {filename}")

if __name__ == "__main__":
    main()
