"""'update_like_post_relation'

Revision ID: e926f1d966ab
Revises: 0ba9d16e1f56
Create Date: 2018-11-03 09:23:21.817079

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e926f1d966ab'
down_revision = '0ba9d16e1f56'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('like_post')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('like_post',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('post_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('user_id', mysql.VARCHAR(length=100), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], name='like_post_ibfk_1'),
    sa.ForeignKeyConstraint(['user_id'], ['front_user.id'], name='like_post_ibfk_2'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
