import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from parser import parse_log
from analyzer import analyze_kpis
from plotter import plot_kpis
import pandas as pd

df_global = None


def browse_file():
    global df_global
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if not filepath:
        return

    try:
        data = parse_log(filepath)
        df_global = analyze_kpis(data,
                                 rsrp_thresh=int(rsrp_var.get()),
                                 sinr_thresh=int(sinr_var.get()),
                                 cqi_thresh=int(cqi_var.get()))

        text.delete("1.0", tk.END)
        text.insert(tk.END, df_global.to_string(index=False))
        plot_kpis(df_global)

        df_global.to_csv("report.csv", index=False)
        messagebox.showinfo("Done", "Analysis complete. CSV saved.")

    except Exception as e:
        messagebox.showerror("Error", str(e))


def export_excel():
    if df_global is not None:
        df_global.to_excel("report.xlsx", index=False)
        messagebox.showinfo("Exported", "Saved to report.xlsx")
    else:
        messagebox.showerror("No data", "Run analysis first")


root = tk.Tk()
root.title("Modem KPI Analyzer")
root.geometry("950x650")

frame = tk.Frame(root)
frame.pack(pady=10)

# Dropdowns
tk.Label(frame, text="RSRP Threshold").grid(row=0, column=0)
rsrp_var = ttk.Combobox(frame, values=[-110, -105, -100, -95, -90])
rsrp_var.set(-100)
rsrp_var.grid(row=0, column=1)

tk.Label(frame, text="SINR Threshold").grid(row=0, column=2)
sinr_var = ttk.Combobox(frame, values=[10, 15, 18, 20])
sinr_var.set(18)
sinr_var.grid(row=0, column=3)

tk.Label(frame, text="CQI Threshold").grid(row=0, column=4)
cqi_var = ttk.Combobox(frame, values=[4, 5, 6, 7])
cqi_var.set(6)
cqi_var.grid(row=0, column=5)

# Buttons
tk.Button(root, text="Browse Log File", command=browse_file).pack(pady=10)
tk.Button(root, text="Export to Excel", command=export_excel).pack(pady=5)

# Output window
text = tk.Text(root, wrap="none", height=30)
text.pack(expand=True, fill='both', padx=10, pady=10)

root.mainloop()
