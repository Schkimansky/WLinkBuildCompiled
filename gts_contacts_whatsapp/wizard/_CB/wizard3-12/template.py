�
    
�(g�  �                   �8   � d dl mZ ddlmZ g d�Z G d� d�      Zy)�   )�zstring�   )�Config))�sales_quotationszSales Quotation/Order)�purchase_quotationzPurchase Quotation)�invoice�Invoicec                   �^   � e Zd Zdedeeef   fd�Zdee   fd�Ze	dee   dee   fd��       Z
y)	�Template�template_text�pathsc                 �T   � || _         t        j                  |�      | _        || _        y �N)r   r   �TextTemplate�templater   )�selfr   r   s      �wizard/template.py�__init__zTemplate.__init__   s#   � �*����,�,�]�;���%*��
�    �objectsc                 �  � | j                   j                  �       }i }|D ]F  }| j                  j                  |�      }|s�!| j                  ||j	                  d�      �      }|||<   �H | j                   j                  |�      S )N�.)r   �get_variablesr   �get�split�fill)r   r   �	variables�results�var�path�results          r   r   zTemplate.fill   sx   � ��M�M�/�/�1�	�"$��� 	"�C�#�z�z�~�~�c�2�D����X�X�g�t�z�z�#��7�F�!�G�C�L�	"� �}�}�!�!�'�*�*r   �namesc                 �n   � | D ]  }	 |}|D ]  }t        ||�      }� |c S  y # t        t        f$ r Y �0w xY wr   )�getattr�AttributeError�	NameError)r   r"   �object�current�names        r   r   zTemplate.get    sV   � �� 		�F�� ��!� 5�D�%�g�t�4�G�5� ��		�� #�I�.� ���s   �"�4�4N)�__name__�
__module__�__qualname__�str�dictr   �listr'   r   �staticmethodr   � r   r   r   r      sW   � �+�c� +�$�s�C�x�.� +�
+�D��L� +� �
�T�&�\� 
�$�s�)� 
� �
r   r   N)� r   �	global_pyr   �TEMPLATES_SELECTIONr   r1   r   r   �<module>r5      s   �� � �� � �  r   