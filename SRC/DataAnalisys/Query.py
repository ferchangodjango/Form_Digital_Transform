

class Query():

    @classmethod
    def consultingData(self):
        query="""SELECT *
                FROM QUESTIONNAIRE_VALUES"""
        return query
    
    @classmethod
    def queryinsert(self,data):
        query="""INSERT INTO QUESTIONNAIRE_VALUES(COMPANY_NAME,QUESTION_A,
                                                QUESTION_B,QUESTION_C,QUESTION_D,QUESTION_E,
                                                QUESTION_F,QUESTION_G,QUESTION_H,QUESTION_I,
                                                QUESTION_J,QUESTION_K,QUESTION_L,QUESTION_M,
                                                QUESTION_O,QUESTION_P,QUESTION_Q,QUESTION_R,
                                                QUESTION_S,QUESTION_T,QUESTION_U,QUESTION_V)
                VALUES ("{0}",{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},
                        {11},{12},{13},{14},{15},{16},{17},{18},{19},
                        {20},{21})""".format(data['COMPANY_NAME'],
                                            data['QUESTION_A'],data['QUESTION_B'],data['QUESTION_C'],
                                            data['QUESTION_D'],data['QUESTION_E'],data['QUESTION_F'],
                                            data['QUESTION_G'],data['QUESTION_H'],data['QUESTION_I'],
                                            data['QUESTION_J'],data['QUESTION_K'],data['QUESTION_L'],
                                            data['QUESTION_M'],data['QUESTION_O'],data['QUESTION_P'],
                                            data['QUESTION_Q'],data['QUESTION_R'],data['QUESTION_S'],
                                            data['QUESTION_T'],data['QUESTION_U'],data['QUESTION_V'])
        return query

        