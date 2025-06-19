#!/bin/bash

# Obtener el nombre del proyecto (carpeta actual)
nombre_proyecto=$(basename "$PWD")

# Definir ruta remota
ruta_remota="gdrive:/KaliSync/$nombre_proyecto"

# Mensajes informativos
echo "📥 Descargando proyecto '$nombre_proyecto' desde Google Drive..."
echo "☁️  Origen remoto: $ruta_remota"
echo "📁 Destino local: $PWD"
echo "⏳ Descargando solo archivos nuevos o modificados..."

# Descargar archivos desde Google Drive sin borrar nada local
rclone copy -P "$ruta_remota" "$PWD"

# Verificar si la descarga fue exitosa
if [ $? -eq 0 ]; then
    echo "✅ Descarga completada con éxito."
else
    echo "❌ Hubo un error durante la descarga."
fi

