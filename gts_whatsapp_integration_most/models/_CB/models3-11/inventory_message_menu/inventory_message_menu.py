�
    
�(ga  �            	       �*  � d dl Z d dlZd dlmZmZmZ e j        �                    ej        �                    ej        �	                    ej        �
                    e�  �        d�  �        �  �        �  �         d dlmZ ddgZ G d� dej        �  �        ZdS )	�    N)�fields�models�apiz../../)�Config)�stock.action_report_deliveryzDelivery Slip)zstock.action_report_pickingzPicking Operationsc                   �v   � e Zd ZdZdZ ej        eddd��  �        Z e	j
        d�  �        d� �   �         Zd	� Zd
S )�InventoryMessageMenuz whatsapp_contacts.messaging_menuz*whatsapp_contacts.messaging_menu.inventoryTr   �Document)�required�default�string�selected_documentc                 �p   � | j         r.t          | �  �        �                    | j         �  �        | _        d S d S �N)r   r   �get_template_text�message��selfs    �7models/inventory_message_menu/inventory_message_menu.py�onchange_selected_documentz/InventoryMessageMenu.onchange_selected_document   s<   � ��!� 	R�!�$�<�<�9�9�$�:P�Q�Q�D�L�L�L�	R� 	R�    c                 �   � | j         S r   )r   r   s    r   �get_document_namez&InventoryMessageMenu.get_document_name   s   � ��%�%r   N)�__name__�
__module__�__qualname__�_inherit�_namer   �	Selection�	DOCUMENTSr   r   �onchanger   r   � r   r   r	   r	      su   � � � � � �1�H�8�E�(��(��T�Ki�r|�}�}�}���S�\�%�&�&�R� R� '�&�R�&� &� &� &� &r   r	   )�sys�os�odoor   r   r   �path�append�abspath�join�dirname�__file__�	global_pyr   r    �TransientModelr	   r"   r   r   �<module>r.      s�   �� 
�
�
�
� 	�	�	�	� $� $� $� $� $� $� $� $� $� $� ������������R�W�_�_�X�-F�-F�� Q� Q�R�R� S� S� S� � � � � � �>�@u�v�	�&� &� &� &� &�6�0� &� &� &� &� &r   