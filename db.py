import sqlite3

class Equipe:
    def criar():
        conn = sqlite3.connect('II_Taca_CZ_Volei.db')
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS equipes (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(255) NOT NULL,
                representante VARCHAR(255) NOT NULL
            );
        """)
        conn.close()

    def novo_equipe(nome, representante):
        conn = sqlite3.connect('II_Taca_CZ_Volei.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO equipes (nome, representante)
            VALUES (?, ?);
        """, (nome, representante))
        conn.commit()
        conn.close()

    def listar_equipe():
        conn = sqlite3.connect('II_Taca_CZ_Volei.db')
        cursor = conn.cursor()
        values = cursor.execute("SELECT * FROM equipes")
        resultado = []
        for row in values:
            resultado.append({
                'id': row[0],
                'nome': row[1],
                'representante': row[2],
            })
        conn.close()
        return resultado

    def atualiza_equipe(id, nome, representante):
        conn = sqlite3.connect('II_Taca_CZ_Volei.db')
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE equipes
            SET nome=?, representante=?
            WHERE id=?;
            """, (nome, representante, id))

        conn.commit()
        conn.close()

    def remove_equipe(id):
        conn = sqlite3.connect('II_Taca_CZ_Volei.db')
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM equipes
            WHERE id=?;
        """, (id,))
        conn.commit()
        conn.close()

    def detalha_equipe(id):
        conn = sqlite3.connect('II_Taca_CZ_Volei.db')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM equipes
            WHERE id=?;
        """, (id,))
        item = cursor.fetchone()
        conn.close()
        if item is None:
            return None
        return {
            'id': item[0],
            'nome': item[1],
            'representante': item[2],
        }



class Partida:
    def criar():
        conn = sqlite3.connect('II_Taca_CZ_Volei.db')
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS partidas (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                data DATE NOT NULL,
                local VARCHAR(255) NOT NULL
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS partida_equipe (
                id_partida INTEGER NOT NULL,
                id_equipe INTEGER NOT NULL,
                pontos INTEGER NOT NULL,
                FOREIGN KEY(id_partida) REFERENCES partidas(id),
                FOREIGN KEY(id_equipe) REFERENCES equipes(id),
                PRIMARY KEY (id_partida, id_equipe)
            );
        """)
        conn.close()

    def nova_partida(data, local):
        conn = sqlite3.connect('II_Taca_CZ_Volei.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO partidas (data, local)
            VALUES (?, ?);
        """, (data, local))
        conn.commit()
        conn.close()

    def listar_partidas():
        conn = sqlite3.connect('II_Taca_CZ_Volei.db')
        cursor = conn.cursor()
        values = cursor.execute("SELECT * FROM partidas")
        resultado = []
        for row in values:
            resultado.append({
                'id': row[0],
                'data': row[1],
                'local': row[2],
            })
        conn.close()
        return resultado

    def atualiza_partida(id, data, local):
        conn = sqlite3.connect('II_Taca_CZ_Volei.db')
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE partidas
            SET data=?, local=?
            WHERE id=?;
        """, (data, local, id))
        conn.commit()
        conn.close()

    def remove_partida(id):
        conn = sqlite3.connect('II_Taca_CZ_Volei.db')
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM partidas
            WHERE id=?;
        """, (id,))
        conn.commit()
        conn.close()

    def detalha_partida(id):
        conn = sqlite3.connect('II_Taca_CZ_Volei.db')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM partidas
            WHERE id=?;
        """, (id,))
        item = cursor.fetchone()
        conn.close()
        if item is None:
            return None
        return {
            'id': item[0],
            'data': item[1],
            'local': item[2],
        }
        
    def adicionar_equipe(id_partida, id_equipe, pontos):
        conn = sqlite3.connect('II_Taca_CZ_Volei.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO partida_equipe (id_partida, id_equipe, pontos)
            VALUES (?, ?, ?);
        """, (id_partida, id_equipe, pontos))
        conn.commit()
        conn.close()


if __name__ == '__main__':
    Equipe.criar()
    Partida.criar()