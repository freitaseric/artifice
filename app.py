import sys
import os
import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image
from typing import Optional


def resource_path(relative_path: str) -> str:
    try:
        base_path = sys._MEIPASS  # type: ignore
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


LOGO_DATABASE = {"Placeholder": resource_path("logos/placeholder.png")}


class ArtificeApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Artífice v1.1 com Preview")

        self.geometry("1200x700")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(1, weight=1)

        self.base_image_path: Optional[str] = None
        self.base_image_pil: Optional[Image.Image] = None

        self._create_widgets()

    def _create_widgets(self):
        controls_frame = ctk.CTkFrame(self)
        controls_frame.grid(row=0, column=0, rowspan=3, padx=20, pady=20, sticky="nsew")
        controls_frame.grid_columnconfigure(0, weight=1)

        top_frame = ctk.CTkFrame(controls_frame)
        top_frame.grid(row=0, column=0, padx=15, pady=15, sticky="ew")

        self.select_image_button = ctk.CTkButton(
            top_frame, text="1. Selecionar Imagem Base", command=self._on_select_image
        )
        self.select_image_button.pack(side="left", padx=15, pady=15)

        self.image_path_label = ctk.CTkLabel(
            top_frame, text="Nenhuma imagem selecionada...", text_color="gray"
        )
        self.image_path_label.pack(side="left", expand=True, fill="x", padx=15)

        logo_frame = ctk.CTkFrame(controls_frame)
        logo_frame.grid(row=1, column=0, padx=15, pady=15, sticky="ew")
        logo_frame.grid_columnconfigure(3, weight=1)

        ctk.CTkLabel(
            logo_frame, text="2. Configurar Logo:", font=ctk.CTkFont(weight="bold")
        ).grid(row=0, column=0, columnspan=5, padx=15, pady=(15, 5), sticky="w")

        logo_names = list(LOGO_DATABASE.keys())
        self.logo_choice_var = ctk.StringVar(value=logo_names[0])

        self.logo_option_menu = ctk.CTkOptionMenu(
            logo_frame,
            variable=self.logo_choice_var,
            values=logo_names,
            command=lambda _: self._update_preview(),
        )
        self.logo_option_menu.grid(row=1, column=0, padx=15, pady=15)

        ctk.CTkLabel(logo_frame, text="Posição X:").grid(
            row=1, column=1, padx=(20, 5), pady=15
        )
        self.x_entry = ctk.CTkEntry(logo_frame, placeholder_text="ex: 50", width=100)
        self.x_entry.grid(row=1, column=2, padx=0, pady=15)

        self.x_entry.bind("<KeyRelease>", lambda event: self._update_preview())

        ctk.CTkLabel(logo_frame, text="Posição Y:").grid(
            row=1, column=3, padx=(20, 5), pady=15
        )
        self.y_entry = ctk.CTkEntry(logo_frame, placeholder_text="ex: 1800", width=100)
        self.y_entry.grid(row=1, column=4, padx=(0, 15), pady=15)
        self.y_entry.bind("<KeyRelease>", lambda event: self._update_preview())

        bottom_frame = ctk.CTkFrame(controls_frame)
        bottom_frame.grid(row=2, column=0, padx=15, pady=15, sticky="ew")
        self.process_button = ctk.CTkButton(
            bottom_frame,
            text="3. Aplicar Logo e Salvar Imagem",
            command=self._on_process_and_save,
        )
        self.process_button.pack(pady=15, padx=15, fill="x")

        preview_frame = ctk.CTkFrame(self, fg_color="transparent")
        preview_frame.grid(row=0, column=1, rowspan=3, padx=20, pady=20, sticky="nsew")
        preview_frame.grid_rowconfigure(1, weight=1)

        ctk.CTkLabel(
            preview_frame, text="Preview:", font=ctk.CTkFont(size=16, weight="bold")
        ).grid(row=0, column=0, sticky="w")
        self.preview_label = ctk.CTkLabel(
            preview_frame,
            text="Selecione uma imagem para ver o preview",
            text_color="gray",
        )
        self.preview_label.grid(row=1, column=0, sticky="nsew")

        self.status_label = ctk.CTkLabel(self, text="Status: Pronto")
        self.status_label.grid(
            row=3, column=0, columnspan=2, padx=20, pady=10, sticky="w"
        )

    def _on_select_image(self):
        path = filedialog.askopenfilename(
            title="Selecione a imagem base",
            filetypes=[("Imagens", "*.jpg *.jpeg *.png"), ("Todos os arquivos", "*.*")],
        )
        if not path:
            return

        try:
            self.base_image_path = path
            self.base_image_pil = Image.open(path).convert("RGBA")
            self.image_path_label.configure(
                text=os.path.basename(path), text_color="white"
            )
            self.status_label.configure(
                text=f"Status: Imagem '{os.path.basename(path)}' carregada."
            )

            self._update_preview()
        except Exception as e:
            messagebox.showerror(
                "Erro ao Abrir", f"Não foi possível carregar a imagem: {e}"
            )
            self.base_image_path = None
            self.base_image_pil = None

    def _update_preview(self):
        """Função principal para gerar e exibir o preview da imagem."""

        if self.base_image_pil is None:
            return

        try:
            x_pos_str = self.x_entry.get()
            y_pos_str = self.y_entry.get()

            x_pos = int(x_pos_str) if x_pos_str else 0
            y_pos = int(y_pos_str) if y_pos_str else 0
        except (ValueError, TypeError):
            return

        try:
            preview_pil = self.base_image_pil.copy()

            selected_logo_name = self.logo_choice_var.get()
            logo_path = LOGO_DATABASE[selected_logo_name]
            logo_image = Image.open(logo_path).convert("RGBA")

            preview_pil.paste(logo_image, (x_pos, y_pos), logo_image)

            label_w = self.preview_label.winfo_width()
            label_h = self.preview_label.winfo_height()

            if label_w < 50 or label_h < 50:
                label_w, label_h = 600, 600

            preview_pil.thumbnail((label_w, label_h))

            preview_ctk = ctk.CTkImage(
                light_image=preview_pil, dark_image=preview_pil, size=preview_pil.size
            )
            self.preview_label.configure(image=preview_ctk, text="")

        except FileNotFoundError:
            self.preview_label.configure(
                image=None,
                text=f"Erro: Logo não encontrada em\n{logo_path}",
                text_color="red",
            )
        except Exception as e:
            self.preview_label.configure(
                image=None, text=f"Erro no preview:\n{e}", text_color="red"
            )

    def _on_process_and_save(self):
        if not self.base_image_pil:
            messagebox.showerror(
                "Erro de Validação", "Selecione uma imagem base primeiro!"
            )
            return

        try:
            x_pos = int(self.x_entry.get())
            y_pos = int(self.y_entry.get())
        except (ValueError, TypeError):
            messagebox.showerror(
                "Erro de Validação",
                "As posições X e Y devem ser números inteiros válidos.",
            )
            return

        selected_logo_name = self.logo_choice_var.get()
        logo_path = LOGO_DATABASE[selected_logo_name]

        try:
            self.status_label.configure(text="Status: Processando imagem...")
            self.update_idletasks()

            final_image = self.base_image_pil.copy()
            logo_image = Image.open(logo_path).convert("RGBA")
            final_image.paste(logo_image, (x_pos, y_pos), logo_image)

        except FileNotFoundError:
            messagebox.showerror(
                "Erro de Arquivo", f"Arquivo de logo não encontrado em '{logo_path}'"
            )
            self.status_label.configure(text="Status: Erro!")
            return
        except Exception as e:
            messagebox.showerror(
                "Erro de Processamento", f"Ocorreu um erro ao processar a imagem: {e}"
            )
            self.status_label.configure(text="Status: Erro!")
            return

        save_path = filedialog.asksaveasfilename(
            title="Salvar imagem processada como...",
            defaultextension=".png",
            filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg")],
            initialdir="imagens_saida/",
        )

        if not save_path:
            self.status_label.configure(text="Status: Salvamento cancelado.")
            return

        if save_path.lower().endswith((".jpg", ".jpeg")):
            final_image = final_image.convert("RGB")

        final_image.save(save_path)
        self.status_label.configure(
            text=f"Status: Imagem salva com sucesso em {os.path.basename(save_path)}!"
        )
        messagebox.showinfo("Sucesso!", "A logo foi aplicada e a imagem foi salva.")


if __name__ == "__main__":
    app = ArtificeApp()
    app.mainloop()
