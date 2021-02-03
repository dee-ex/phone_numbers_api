"""empty message

Revision ID: 250481aec0ae
Revises: 
Create Date: 2021-02-03 09:47:18.658324

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '250481aec0ae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
  op.create_table(
    'phone_numbers',
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('name', sa.String(255), nullable=False),
    sa.Column('num', sa.String(255), nullable=False),
    sa.Column('subnum', sa.String(255), nullable=False),
    sa.Column('note', sa.String(255), nullable=False),
  )


def downgrade():
  op.drop_table('phone_numbers') 
