o
    �(g�  �                   @   s:   d dl mZmZmZ ddlmZmZ G dd� dej�ZdS )�    )�fields�api�models�   )�Config�get_default_connectionc                       sH   e Zd ZdZejdddd�Zej� fdd��Z	e�
d�d	d
� �Z�  ZS )�SelectConnectionz"gts_whatsapp_pos.select_connectionzwhatsapp.connectionzWhatsapp ConnectionT)�stringZrequiredc                    s*   t t| ��|�}t| d�}|r||d< |S )N�pos_connection�
connection)�superr   �default_getr   )�selfr   �resultr   ��	__class__� �wizard/select_connection.pyr   
   s
   
zSelectConnection.default_getr   c                 C   s"   | j rt| ��d| j j� d S d S )Nr
   )r   r   �set�id)r   r   r   r   �onchange_connection   s   �z$SelectConnection.onchange_connection)�__name__�
__module__�__qualname__�_namer   ZMany2oner   r   Zmodelr   Zonchanger   �__classcell__r   r   r   r   r      s    
r   N)	Zodoor   r   r   Z	global_pyr   r   ZTransientModelr   r   r   r   r   �<module>   s    