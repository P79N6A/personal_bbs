"""'add_commentModel'

Revision ID: 505feb0e9852
Revises: 8c5ce68188c1
Create Date: 2018-10-29 10:44:12.788560

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '505feb0e9852'
down_revision = '8c5ce68188c1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=200), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('commenter_id', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['commenter_id'], ['front_user.id'], ),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comment')
    # ### end Alembic commands ###