�
    	�(g�  �                   �L   � d dl mZmZmZ ddlmZ  G d� dej        �  �        ZdS )�    )�fields�models�api�   )�	global_pyc                   �   � e Zd ZdZd� Zd� ZdS )�PurchaseOrderzpurchase.orderc                 �2   � t          j        | ddd��  �        S )NT�purchase_quotationz"purchase.report_purchase_quotation)�template_mode�template_name�document_name�r   �generate_payload��selfs    �models/purchase.py�whatsapp_template_messagez'PurchaseOrder.whatsapp_template_message   s.   � ��)�$�d�Rf�  w[�  \�  \�  \�  	\�    c                 �.   � t          j        | d��  �        S )NF)r   r   r   s    r   �whatsapp_direct_messagez%PurchaseOrder.whatsapp_direct_message   s   � ��)�$�e�D�D�D�Dr   N)�__name__�
__module__�__qualname__�_inheritr   r   � r   r   r	   r	      s?   � � � � � ��H�\� \� \�E� E� E� E� Er   r	   N)�odoor   r   r   � r   �Modelr	   r   r   r   �<module>r       su   �� $� $� $� $� $� $� $� $� $� $� � � � � � �E� E� E� E� E�F�L� E� E� E� E� Er   