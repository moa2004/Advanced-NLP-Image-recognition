import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, colorchooser
from tkinter import ttk
from PIL import Image, ImageTk, ImageEnhance, ImageOps, ImageDraw, ImageFont

try:
    import pytesseract
    OCR_AVAILABLE = True
except ImportError:
    OCR_AVAILABLE = False

def ent(event):
    event.widget['background'] = event.widget.hover_bg

def leave(event):
    event.widget['background'] = event.widget.default_bg

class CreateToolTip:
    def __init__(self, widget, text):
        self.waittime = 500
        self.wraplength = 180
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None
    def enter(self, event=None):
        self.schedule()
    def leave(self, event=None):
        self.unschedule()
        self.hidetip()
    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)
    def unschedule(self):
        id_ = self.id
        self.id = None
        if id_:
            self.widget.after_cancel(id_)
    def showtip(self, event=None):
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        self.tw = tk.Toplevel(self.widget)
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry(f"+{x}+{y}")
        label = tk.Label(self.tw, text=self.text, justify='left', background="#ffffe0", relief='solid', borderwidth=1, wraplength=self.wraplength, font=("Segoe UI", 9))
        label.pack(ipadx=1)
    def hidetip(self):
        if self.tw:
            self.tw.destroy()
        self.tw = None

class caption:
    def __init__(self, parent):
        self.parent = parent
        self.frame = tk.Frame(parent, bg="#ffffff")
        self.frame.pack(fill="both", expand=True, padx=20, pady=20)
        self.upload_btn = tk.Button(self.frame, text="Upload Image", command=self.up, bg="#4CAF50", fg="white", activebackground="#43A047", font=("Segoe UI", 12, "bold"), relief="flat", bd=0, padx=10, pady=5)
        self.upload_btn.default_bg = "#4CAF50"
        self.upload_btn.hover_bg = "#43A047"
        self.upload_btn.bind("<Enter>", ent)
        self.upload_btn.bind("<Leave>", leave)
        self.upload_btn.pack(pady=15)
        CreateToolTip(self.upload_btn, "Click to upload an image for caption generation")
        self.img_label = tk.Label(self.frame, bg="#ffffff")
        self.img_label.pack(pady=10)
        self.result_text = tk.Text(self.frame, width=80, height=10, font=("Segoe UI", 11), bg="#f9f9f9", fg="#333333", relief="solid", bd=1)
        self.result_text.pack(pady=15)
    def up(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
        if file_path:
            self.image = Image.open(file_path).convert("RGB")
            self.disp(self.image)
            ocr_text = self.ext(self.image)
            description = self.gen(self.image)
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Detected Text:\n" + ocr_text + "\n\nDescription:\n" + description)
    def disp(self, img):
        img = img.resize((300, 300))
        self.tk_img = ImageTk.PhotoImage(img)
        self.img_label.config(image=self.tk_img)
        self.img_label.image = self.tk_img
    def ext(self, img):
        if OCR_AVAILABLE:
            return pytesseract.image_to_string(img)
        return "No OCR Engine Available"
    def gen(self, img):
        return "The image displays a vivid scene with clear details, balanced lighting, and defined subjects, capturing the essence of its moment in a realistic and engaging manner."

class process:
    def __init__(self, parent):
        self.parent = parent
        self.frame = tk.Frame(parent, bg="#ffffff")
        self.frame.pack(fill="both", expand=True, padx=20, pady=20)
        self.upload_btn = tk.Button(self.frame, text="Upload Image", command=self.up, bg="#2196F3", fg="white", activebackground="#1976D2", font=("Segoe UI", 12, "bold"), relief="flat", bd=0, padx=10, pady=5)
        self.upload_btn.default_bg = "#2196F3"
        self.upload_btn.hover_bg = "#1976D2"
        self.upload_btn.bind("<Enter>", ent)
        self.upload_btn.bind("<Leave>", leave)
        self.upload_btn.pack(pady=15)
        CreateToolTip(self.upload_btn, "Click to upload an image for processing")
        self.img_label = tk.Label(self.frame, bg="#ffffff")
        self.img_label.pack(pady=10)
        self.slider_frame = tk.Frame(self.frame, bg="#ffffff")
        self.slider_frame.pack(pady=15)
        self.brightness_scale = tk.Scale(self.slider_frame, from_=0.5, to=2.0, resolution=0.1, orient=tk.HORIZONTAL, label="Brightness", command=lambda val: self.update(), font=("Segoe UI", 10), bg="#ffffff", fg="#333333", troughcolor="#e0e0e0")
        self.brightness_scale.set(1.0)
        self.brightness_scale.grid(row=0, column=0, padx=10)
        self.contrast_scale = tk.Scale(self.slider_frame, from_=0.5, to=2.0, resolution=0.1, orient=tk.HORIZONTAL, label="Contrast", command=lambda val: self.update(), font=("Segoe UI", 10), bg="#ffffff", fg="#333333", troughcolor="#e0e0e0")
        self.contrast_scale.set(1.0)
        self.contrast_scale.grid(row=0, column=1, padx=10)
        self.saturation_scale = tk.Scale(self.slider_frame, from_=0.5, to=2.0, resolution=0.1, orient=tk.HORIZONTAL, label="Saturation", command=lambda val: self.update(), font=("Segoe UI", 10), bg="#ffffff", fg="#333333", troughcolor="#e0e0e0")
        self.saturation_scale.set(1.0)
        self.saturation_scale.grid(row=0, column=2, padx=10)
        self.reset_btn = tk.Button(self.frame, text="Reset", command=self.reset, bg="#f44336", fg="white", activebackground="#d32f2f", font=("Segoe UI", 12, "bold"), relief="flat", bd=0, padx=10, pady=5)
        self.reset_btn.default_bg = "#f44336"
        self.reset_btn.hover_bg = "#d32f2f"
        self.reset_btn.bind("<Enter>", ent)
        self.reset_btn.bind("<Leave>", leave)
        self.reset_btn.pack(pady=15)
        CreateToolTip(self.reset_btn, "Reset the image to its original state")
    def up(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
        if file_path:
            self.original_image = Image.open(file_path).convert("RGB")
            self.disp(self.original_image)
    def update(self):
        if hasattr(self, "original_image"):
            img = self.original_image.copy()
            b_val = self.brightness_scale.get()
            c_val = self.contrast_scale.get()
            s_val = self.saturation_scale.get()
            img = ImageEnhance.Brightness(img).enhance(b_val)
            img = ImageEnhance.Contrast(img).enhance(c_val)
            img = ImageEnhance.Color(img).enhance(s_val)
            self.disp(img)
    def reset(self):
        self.brightness_scale.set(1.0)
        self.contrast_scale.set(1.0)
        self.saturation_scale.set(1.0)
        if hasattr(self, "original_image"):
            self.disp(self.original_image)
    def disp(self, img):
        img = img.resize((300, 300))
        self.tk_img = ImageTk.PhotoImage(img)
        self.img_label.config(image=self.tk_img)
        self.img_label.image = self.tk_img

class Extra:
    def __init__(self, parent):
        self.parent = parent
        self.frame = tk.Frame(parent, bg="#ffffff")
        self.frame.pack(fill="both", expand=True, padx=20, pady=20)
        self.title = tk.Label(self.frame, text="Extra Tools", font=("Segoe UI", 16, "bold"), bg="#ffffff", fg="#4CAF50")
        self.title.pack(pady=10)
        self.desc = tk.Label(self.frame, text="Enhance your project with these powerful tools:", font=("Segoe UI", 12), bg="#ffffff", fg="#333333")
        self.desc.pack(pady=5)
        self.btn_frame = tk.Frame(self.frame, bg="#ffffff")
        self.btn_frame.pack(pady=10)
        self.meta_btn = tk.Button(self.btn_frame, text="Image Metadata", command=self.show_metadata, bg="#9C27B0", fg="white", activebackground="#7B1FA2", font=("Segoe UI", 11, "bold"), relief="flat", bd=0, padx=10, pady=5)
        self.meta_btn.default_bg = "#9C27B0"
        self.meta_btn.hover_bg = "#7B1FA2"
        self.meta_btn.bind("<Enter>", ent)
        self.meta_btn.bind("<Leave>", leave)
        self.meta_btn.grid(row=0, column=0, padx=10, pady=10)
        self.color_btn = tk.Button(self.btn_frame, text="Color Palette Extractor", command=self.extract_palette, bg="#E91E63", fg="white", activebackground="#C2185B", font=("Segoe UI", 11, "bold"), relief="flat", bd=0, padx=10, pady=5)
        self.color_btn.default_bg = "#E91E63"
        self.color_btn.hover_bg = "#C2185B"
        self.color_btn.bind("<Enter>", ent)
        self.color_btn.bind("<Leave>", leave)
        self.color_btn.grid(row=0, column=1, padx=10, pady=10)
        self.filter_btn = tk.Button(self.btn_frame, text="Filter Preview", command=self.filter_preview, bg="#FF9800", fg="white", activebackground="#F57C00", font=("Segoe UI", 11, "bold"), relief="flat", bd=0, padx=10, pady=5)
        self.filter_btn.default_bg = "#FF9800"
        self.filter_btn.hover_bg = "#F57C00"
        self.filter_btn.bind("<Enter>", ent)
        self.filter_btn.bind("<Leave>", leave)
        self.filter_btn.grid(row=1, column=0, padx=10, pady=10)
        self.watermark_btn = tk.Button(self.btn_frame, text="Add Watermark", command=self.add_watermark, bg="#03A9F4", fg="white", activebackground="#0288D1", font=("Segoe UI", 11, "bold"), relief="flat", bd=0, padx=10, pady=5)
        self.watermark_btn.default_bg = "#03A9F4"
        self.watermark_btn.hover_bg = "#0288D1"
        self.watermark_btn.bind("<Enter>", ent)
        self.watermark_btn.bind("<Leave>", leave)
        self.watermark_btn.grid(row=1, column=1, padx=10, pady=10)
    def show_metadata(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
        if file_path:
            try:
                img = Image.open(file_path)
            except:
                messagebox.showerror("Error", "Could not open image file.")
                return
            metadata = f"Format: {img.format}\nSize: {img.size}\nMode: {img.mode}\nInfo: {img.info}"
            meta_win = tk.Toplevel(self.frame)
            meta_win.title("Image Metadata")
            text = tk.Text(meta_win, wrap="word", font=("Segoe UI", 10))
            text.insert(tk.END, metadata)
            text.pack(expand=True, fill="both", padx=10, pady=10)
    def extract_palette(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
        if file_path:
            try:
                img = Image.open(file_path)
            except:
                messagebox.showerror("Error", "Could not open image file.")
                return
            img_small = img.resize((150,150))
            result = img_small.convert("P", palette=Image.ADAPTIVE, colors=10)
            palette = result.getpalette()
            color_counts = sorted(result.getcolors(), reverse=True)
            colors = []
            for count, index in color_counts:
                r = palette[index*3]
                g = palette[index*3+1]
                b = palette[index*3+2]
                color = (r, g, b)
                if color not in colors:
                    colors.append(color)
                if len(colors) >= 5:
                    break
            pal_win = tk.Toplevel(self.frame)
            pal_win.title("Color Palette")
            for i, color in enumerate(colors):
                hex_color = '#%02x%02x%02x' % color
                frame = tk.Frame(pal_win, bg=hex_color, width=100, height=100)
                frame.grid(row=0, column=i, padx=10, pady=10)
                label = tk.Label(pal_win, text=hex_color, font=("Segoe UI", 10))
                label.grid(row=1, column=i, padx=10)
    def filter_preview(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
        if file_path:
            try:
                img = Image.open(file_path)
            except:
                messagebox.showerror("Error", "Could not open image file.")
                return
            img_gray = ImageOps.grayscale(img)
            filt_win = tk.Toplevel(self.frame)
            filt_win.title("Filter Preview")
            orig_img = img.resize((300,300))
            gray_img = img_gray.resize((300,300))
            tk_orig = ImageTk.PhotoImage(orig_img)
            tk_gray = ImageTk.PhotoImage(gray_img)
            orig_label = tk.Label(filt_win, image=tk_orig)
            orig_label.image = tk_orig
            orig_label.pack(side="left", padx=10, pady=10)
            gray_label = tk.Label(filt_win, image=tk_gray)
            gray_label.image = tk_gray
            gray_label.pack(side="right", padx=10, pady=10)
    def add_watermark(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
        if not file_path:
            return
        try:
            img = Image.open(file_path)
        except:
            messagebox.showerror("Error", "Could not open image file.")
            return
        watermark_text = simpledialog.askstring("Watermark Text", "Enter watermark text:")
        if not watermark_text:
            return
        color_choice = colorchooser.askcolor(title="Choose Watermark Text Color")
        if color_choice[1] is None:
            watermark_color = (255,255,255,200)
        else:
            hex_color = color_choice[1]
            watermark_color = (int(hex_color[1:3],16), int(hex_color[3:5],16), int(hex_color[5:7],16), 200)
        try:
            font = ImageFont.truetype("arial.ttf", 36)
        except:
            font = ImageFont.load_default()
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        txt_layer = Image.new('RGBA', img.size, (255,255,255,0))
        draw = ImageDraw.Draw(txt_layer)
        bbox = draw.textbbox((0,0), watermark_text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        padding = 10
        x = img.width - text_width - padding
        y = img.height - text_height - padding
        draw.text((x, y), watermark_text, font=font, fill=watermark_color)
        watermarked = Image.alpha_composite(img, txt_layer)
        watermarked_win = tk.Toplevel(self.frame)
        watermarked_win.title("Watermarked Image")
        disp_img = watermarked.convert("RGB").resize((300,300))
        tk_img = ImageTk.PhotoImage(disp_img)
        label = tk.Label(watermarked_win, image=tk_img)
        label.image = tk_img
        label.pack(padx=10, pady=10)
        save_btn = tk.Button(watermarked_win, text="Save Watermarked Image", command=lambda: self.save_watermarked(watermarked), bg="#4CAF50", fg="white", activebackground="#388E3C", font=("Segoe UI", 11, "bold"), relief="flat", bd=0, padx=10, pady=5)
        save_btn.pack(pady=5)
    def save_watermarked(self, img):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg;*.jpeg")])
        if file_path:
            try:
                img.convert("RGB").save(file_path)
                messagebox.showinfo("Success", "Image saved successfully!")
            except:
                messagebox.showerror("Error", "Failed to save image.")

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Caption Generator")
        self.root.geometry("1000x900")
        self.root.configure(bg="#f0f0f0")
        self.menu()
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TNotebook", background="#f0f0f0", borderwidth=0)
        style.configure("TNotebook.Tab", background="#d9d9d9", foreground="#333333", padding=[10, 5], font=("Segoe UI", 11, "bold"))
        style.map("TNotebook.Tab", background=[("selected", "#4CAF50")], foreground=[("selected", "white")])
        title_label = tk.Label(root, text="ImageCaptionPro", font=("Segoe UI", 24, "bold"), bg="#f0f0f0", fg="#333333")
        title_label.pack(pady=10)
        self.notebook = ttk.Notebook(root)
        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.tab3 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Caption Generator")
        self.notebook.add(self.tab2, text="Image Processor")
        self.notebook.add(self.tab3, text="Extra")
        self.notebook.pack(expand=1, fill="both", padx=20, pady=20)
        self.caption_tab = caption(self.tab1)
        self.processor_tab = process(self.tab2)
        self.extra_tab = Extra(self.tab3)
    def menu(self):
        menubar = tk.Menu(self.root, font=("Segoe UI", 10))
        filemenu = tk.Menu(menubar, tearoff=0, font=("Segoe UI", 10))
        filemenu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        helpmenu = tk.Menu(menubar, tearoff=0, font=("Segoe UI", 10))
        helpmenu.add_command(label="About", command=self.about)
        menubar.add_cascade(label="Help", menu=helpmenu)
        self.root.config(menu=menubar)
    def about(self):
        messagebox.showinfo("About", "ImageCaptionPro\nVersion 1.0\nDeveloped with A'MMM Gonna kill my self team")

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
