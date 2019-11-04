"""empty message

Revision ID: d8db7dd89fd0
Revises: b735968fdef0
Create Date: 2019-11-04 16:00:10.297716

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd8db7dd89fd0'
down_revision = 'b735968fdef0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wallet_transactions')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('wallet_transactions',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('trans_time', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('trans_id', mysql.VARCHAR(length=220), nullable=True),
    sa.Column('trans_status', mysql.VARCHAR(length=220), nullable=True),
    sa.Column('paypal_payer_email', mysql.VARCHAR(length=220), nullable=True),
    sa.Column('paypal_payer_name', mysql.VARCHAR(length=220), nullable=True),
    sa.Column('paypal_payer_surname', mysql.VARCHAR(length=220), nullable=True),
    sa.Column('paypal_payer_id', mysql.VARCHAR(length=220), nullable=True),
    sa.Column('old_amount', mysql.FLOAT(), nullable=True),
    sa.Column('trans_amount', mysql.FLOAT(), nullable=True),
    sa.Column('new_amount', mysql.FLOAT(), nullable=True),
    sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('user_email', mysql.VARCHAR(length=220), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
