�
    ?�,g�  �                   �L   � d dl mZmZmZ ddlmZ  G d� dej        �  �        ZdS )�    )�fields�models�api�   )�	global_pyc                   �   � e Zd ZdZd� Zd� ZdS )�	SaleOrderz
sale.orderc                 �2   � t          j        | ddd��  �        S )NT�sales_quotationszsale.action_report_saleorder)�template_mode�template_name�document_name�r   �generate_payload��selfs    �models/sale.py�whatsapp_template_messagez#SaleOrder.whatsapp_template_message   s.   � ��)�$�d�Rd�  uS�  T�  T�  T�  	T�    c                 �.   � t          j        | d��  �        S )NF)r   r   r   s    r   �whatsapp_direct_messagez!SaleOrder.whatsapp_direct_message   s   � ��)�$�e�D�D�D�Dr   N)�__name__�
__module__�__qualname__�_inheritr   r   � r   r   r	   r	      s?   � � � � � ��H�T� T� T�E� E� E� E� Er   r	   N)�odoor   r   r   � r   �Modelr	   r   r   r   �<module>r       su   �� $� $� $� $� $� $� $� $� $� $� � � � � � �E� E� E� E� E��� E� E� E� E� Er   