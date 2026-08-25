import json
import os
import glob

def analisis_real_instagram_completo_tres_listas():
    file_following = 'following.json'
    files_followers = glob.glob('followers_*.json')
    
    if not os.path.exists(file_following) or not files_followers:
        print("❌ Error: Falta el archivo following.json o no hay archivos followers_X.json")
        return

    print("⏳ Procesando tus 3 listas definitivas...")
    
    try:
        # 1. Extraer SIGUIENDO (Ignorando cuentas eliminadas)
        with open(file_following, 'r', encoding='utf-8') as f:
            data_following = json.load(f)
            
        siguiendo = set()
        items_following = data_following.get('relationships_following', [])
        for item in items_following:
            u_name = item.get('title')
            if u_name:
                u_name_clean = u_name.strip().lower()
                if 'deleted' not in u_name_clean:
                    siguiendo.add(u_name_clean)
                        
        # 2. Extraer SEGUIDORES (Ignorando cuentas eliminadas)
        seguidores = set()
        for file_f in files_followers:
            with open(file_f, 'r', encoding='utf-8') as f:
                data_followers = json.load(f)
            
            items_followers = data_followers if isinstance(data_followers, list) else []
            for item in items_followers:
                if 'string_list_data' in item:
                    for string_data in item['string_list_data']:
                        val = string_data.get('value')
                        if val:
                            val_clean = val.strip().lower()
                            if 'deleted' not in val_clean:
                                seguidores.add(val_clean)

        # 3. Operaciones matemáticas de conjuntos para las 3 listas
        no_te_siguen = siguiendo - seguidores        # Vos los seguís, ellos a vos no
        mutuos = siguiendo & seguidores              # Se siguen mutuamente (Amigos)
        no_los_seguis = seguidores - siguiendo       # Ellos te siguen, vos a ellos no

        # GENERAR ARCHIVO TXT CON LAS 3 SECCIONES
        nombre_reporte = "reporte_instagram.txt"
        with open(nombre_reporte, 'w', encoding='utf-8') as f_out:
            f_out.write("============================================================\n")
            f_out.write(f"📊 REPORTE DE CONEXIONES COMPLETO\n")
            f_out.write(f"   • Seguidores válidos: {len(seguidores)}\n")
            f_out.write(f"   • Seguidos válidos: {len(siguiendo)}\n")
            f_out.write("============================================================\n\n")
            
            # LISTA 1: Vos seguís, ellos no
            f_out.write(f"❌ 1. CUENTAS QUE VOS SEGUÍS PERO NO TE SIGUEN ({len(no_te_siguen)}):\n")
            if no_te_siguen:
                for idx, usuario in enumerate(sorted(no_te_siguen), 1):
                    f_out.write(f"   {idx}. {usuario}\n")
            else:
                f_out.write("   🎉 ¡Ninguna! Todos te siguen de vuelta.\n")
                    
            f_out.write("\n" + "-"*60 + "\n\n")
            
            # LISTA 2: Mutuos (Se siguen mutuamente)
            f_out.write(f"🤝 2. SEGUIMIENTO MUTUO / AMIGOS ({len(mutuos)}):\n")
            if mutuos:
                for idx, usuario in enumerate(sorted(mutuos), 1):
                    f_out.write(f"   {idx}. {usuario}\n")
            else:
                f_out.write("   👀 No tenés seguimientos mutuos.\n")
                
            f_out.write("\n" + "-"*60 + "\n\n")
            
            # LISTA 3: Ellos te siguen, vos no
            f_out.write(f"⭐ 3. PERSONAS QUE TE SIGUEN PERO QUE VOS NO SEGUÍS ({len(no_los_seguis)}):\n")
            if no_los_seguis:
                for idx, usuario in enumerate(sorted(no_los_seguis), 1):
                    f_out.write(f"   {idx}. {usuario}\n")
            else:
                f_out.write("   👤 ¡Ninguna! Seguís a absolutamente todos tus seguidores.\n")
                
            f_out.write("\n============================================================\n")

        print("\n" + "="*50)
        print("✅ ¡Reporte de 3 listas completado con éxito!")
        print(f"📁 Archivo actualizado: '{nombre_reporte}'")
        print(f"📊 No te siguen: {len(no_te_siguen)} | Mutuos: {len(mutuos)} | No los seguís: {len(no_los_seguis)}")
        print("="*50 + "\n")
        
    except Exception as e:
        print(f"❌ Error al procesar los datos: {e}")

if __name__ == '__main__':
    analisis_real_instagram_completo_tres_listas()