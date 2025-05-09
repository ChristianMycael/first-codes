import svgwrite

# Criar um novo arquivo SVG
svg_detailed_path = "trofeu_detalhado.svg"
dwg = svgwrite.Drawing(svg_detailed_path, profile='tiny', size=("600px", "800px"))

# Corpo do troféu (transparente)
dwg.add(dwg.polygon(
    points=[(150, 100), (450, 100), (500, 600), (100, 600)], 
    fill="none", stroke="black", stroke_width=2, id="corpo_transparente"
))

# Detalhes dourados (asas laterais)
dwg.add(dwg.path(d="M150,100 C50,200 50,400 100,500", fill="none", stroke="gold", stroke_width=5, id="asa_esquerda"))
dwg.add(dwg.path(d="M450,100 C550,200 550,400 500,500", fill="none", stroke="gold", stroke_width=5, id="asa_direita"))

# Base do troféu (preta)
dwg.add(dwg.rect(insert=(180, 600), size=(240, 80), fill="black", stroke="black", stroke_width=3, id="base"))

# Texto "CAMPEÃO" na base (como peça separada)
dwg.add(dwg.text("CAMPEÃO", insert=(230, 650), fill="white", font_size="30px", font_weight="bold", id="texto_campeao"))

# Salvar o arquivo SVG
dwg.save()

print(f"Arquivo SVG salvo como: {svg_detailed_path}")
