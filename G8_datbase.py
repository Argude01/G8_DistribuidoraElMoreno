import mysql.connector


data=[]

class MyDatabase:
    def open_connection(self):
        connection = mysql.connector.connect( 
            host="localhost",                    
            user="root", 
            passwd="", 
            database="db_lol")
        return connection





#ENVIO DE ARTICULOS

    

    def insert_db1(self, nombre_de_articulo, precio_unitario, id_area):
        my_connection = self.open_connection()
        cursor = my_connection.cursor()
        query = "INSERT INTO tbl_articulos( `NOMBRE DE ARTICULO`, `PRECIO UNITARIO`, `ID_AREA`) VALUES (%s,%s,%s)"
        data = ( nombre_de_articulo, precio_unitario, id_area)
        cursor.execute(query, data)
        my_connection.commit()
        my_connection.close()

    def read_db1(self):
            my_connection = self.open_connection()
            cursor = my_connection.cursor()
            query = "SELECT `NOMBRE DE ARTICULO`, `PRECIO UNITARIO`, `ID_AREA` FROM TBL_ARTICULOS"
            cursor.execute(query)
            registro = 0
            for fila in cursor:
                data.append(fila) 
                print('for - ' + str(registro) +" - "+ str(data[registro]))
                registro = registro + 1 
            
            my_connection.close()     
            #print(data)






#PROVEEDORES


    def insert_db2(self, empresa, nombre, apellido, id_pais):
        my_connection = self.open_connection()
        cursor = my_connection.cursor()
        query = "INSERT INTO tbl_provedores (EMPRESA, NOMBRE, APELLIDO, ID_PAIS) VALUES (%s, %s, %s, %s)"
        data = ( empresa, nombre, apellido, id_pais)
        cursor.execute(query, data)
        my_connection.commit()
        my_connection.close()




    
#SUCURSALES

    def insert_db(self, nombre_sucursal, id_pais, id_estado, ubicacion, nombre_gerente, telelfono):
        my_connection = self.open_connection()
        cursor = my_connection.cursor()
        query = "INSERT INTO tbl_sucursales (NOMBRE_SUCURSAL, ID_PAIS, ID_ESTADO, UBICACION, NOMBRE_GERENTE, TELEFONO) VALUES (%s, %s, %s, %s,%s, %s )"
        data = ( nombre_sucursal, id_pais, id_estado, ubicacion, nombre_gerente, telelfono)
        cursor.execute(query, data)
        my_connection.commit()
        my_connection.close()