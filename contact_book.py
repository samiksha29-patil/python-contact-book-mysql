from contact import Contact
from db_config import get_connection

class ContactBook:
    def add_contact(self,contact):
        conn=get_connection()
        cursor=conn.cursor()
        query="INSERT INTO contacts (name,phone,email)VALUES(%s,%s,%s)"
        cursor.execute(query,(contact.name,contact.phone,contact.email))
        conn.commit()
        cursor.close()
        conn.close()
    def display_all_contacts(self):
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT name,phone,email FROM contacts")
        rows=cursor.fetchall()
        if not rows:
            print("No contacts to display.")
        for row in rows:
            contact=Contact(*row)
            contact.display_contact()
        cursor.close()
        conn.close()

    def search_contact(self,name):
        conn=get_connection()
        cursor=conn.cursor()
        query="SELECT name,phone,email FROM contacts WHERE LOWER(name)=LOWER(%s)"
        cursor.execute(query,(name,))
        row=cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            return Contact(*row)
        return None
    def update_contact(self,name,new_name=None,new_phone=None,new_email=None):
        contact=self.search_contact(name)
        if contact:
            updated_name=new_name if new_name else contact.name
            updated_phone=new_phone if new_phone else contact.phone
            updated_email=new_email if new_email else contact.email
            
            conn=get_connection()
            cursor=conn.cursor()
            query="UPDATE contacts SET name=%s,phone=%s, email=%s WHERE LOWER(name)=LOWER(%s)"
            cursor.execute(query,(updated_name,updated_phone,updated_email,name))
            conn.commit()
            cursor.close()
            conn.close()
            print(f" Contact {name} has been updated.")
        else:
            print(f"Contact'{name}'not found.")
        
    def delete_contact(self,name):
        conn=get_connection()
        cursor=conn.cursor()
        query="DELETE FROM contacts WHERE LOWER(name)=LOWER(%s)"
        cursor.execute(query,(name,))
        if cursor.rowcount>0:
            print(f"Contact'{name}'has been deleted.")
        else:
            print(f"Contact'{name}'not found.")
        conn.commit()
        cursor.close()
        conn.close()
                




