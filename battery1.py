import pandas as pd
import plotly.express as px
import plotly.io as pio


metadata_path = '/Users/nidhi/Downloads/cleaned_dataset/metadata.csv'
metadata_df = pd.read_csv(metadata_path)


metadata_df.head()

impedance_df = metadata_df[metadata_df['type'] == 'impedance'].copy()


impedance_df['Re'] = pd.to_numeric(impedance_df['Re'], errors='coerce')
impedance_df['Rct'] = pd.to_numeric(impedance_df['Rct'], errors='coerce')


impedance_df['Cycle'] = impedance_df['uid']


fig_re = px.line(impedance_df, x='Cycle', y='Re', 
                 title='Electrolyte Resistance (Re) vs Cycle',
                 labels={'Cycle': 'Cycle Number', 'Re': 'Electrolyte Resistance (Ohms)'},
                 markers=True)


fig_rct = px.line(impedance_df, x='Cycle', y='Rct', 
                  title='Charge Transfer Resistance (Rct) vs Cycle',
                  labels={'Cycle': 'Cycle Number', 'Rct': 'Charge Transfer Resistance (Ohms)'},
                  markers=True)

fig_re.show(), fig_rct.show()


re_plot_path = "/mnt/data/re_vs_cycle.html"
rct_plot_path = "/mnt/data/rct_vs_cycle.html"

pio.write_html(fig_re, file=re_plot_path, auto_open=False)
pio.write_html(fig_rct, file=rct_plot_path, auto_open=False)

(re_plot_path, rct_plot_path)