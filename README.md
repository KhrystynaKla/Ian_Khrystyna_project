# Ian_Khrystyna_project
sql = '''UPDATE users SET words = ?
        WHERE id = ?
        '''
        CURSOR.execute(sql, [self.join_words(), self.id])
        #GIT ADD
        CONN.commit()
        # updates the row based on current attributes 



        sql = '''UPDATE users SET words = ?
        WHERE id = ?
        '''
        CURSOR.execute(sql, [self.join_words(), self.id])
        #GIT ADD
        CONN.commit()
        # updates the row based on current attributes 