o
    ˎ(g�  �                   @   s6   d dl mZmZmZ ddlmZ G dd� dej�ZdS )�    )�fields�models�api�   )�	global_pyc                   @   s    e Zd ZdZdd� Zdd� ZdS )�	Inventoryzstock.pickingc                 C   s   t j| ddddd�S )Nz*whatsapp_contacts.messaging_menu.inventoryTZinvoicezstock.action_report_picking)Zmodel�template_modeZtemplate_nameZdocument_name�r   Zgenerate_payload��self� r   �models/inventory.py�whatsapp_template_message   s   z#Inventory.whatsapp_template_messagec                 C   s   t j| dd�S )NF)r   r	   r
   r   r   r   �whatsapp_direct_message   s   z!Inventory.whatsapp_direct_messageN)�__name__�
__module__�__qualname__Z_inheritr   r   r   r   r   r   r      s    r   N)Zodoor   r   r   � r   ZModelr   r   r   r   r   �<module>   s    