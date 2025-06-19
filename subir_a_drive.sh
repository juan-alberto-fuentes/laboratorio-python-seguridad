#!/bin/bash

# Obtener el nombre de la carpeta actual (nombre del proyecto)
nombre_proyecto=$(basename "$PWD")

# Ruta remota de destino
ruta_remota="gdrive:/KaliSync/$nombre_proyecto"

# Mensaje de inicio
echo "📤 Subiendo proyecto '$nombre_proyecto' a Google Drive..."
echo "📁 Origen: $PWD"
echo "☁️  Destino: $ruta_remota"
echo "⏳ Procesando solo archivos nuevos o modificados..."

# Comando rclone
rclone copy -P "$PWD" "$ruta_remota"

# Verificación de salida
if [ $? -eq 0 ]; then
    echo "✅ Subida completada con éxito."
else
    echo "❌ Hubo un error durante la subida."
fi

