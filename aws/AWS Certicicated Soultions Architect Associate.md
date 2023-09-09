# AWS Certificated Solutions Architect Associate

**AWS 자격증 Udemy 강의 요약** 



# Section 04. IAM

### IAM Section 

- IAM: Idenitity and Access Management => 글로벌 서비스
- 루트 계정
  - 기본으로 생성
  - 오직 계정을 생성할 때만 사용되어야 하며, 그 후에는 루트 계정을 더 이상 사용해서도, 공유해서도 안됨
- 사용자 생성
  - 하나의 사용자는 조직 내의 한 사람에 해당
  - 필요하다면 사용자들을 그룹으로 묶을 수 있음
- 그룹
  - 그룹에는 사용자만 배치할 수 있으며, 다른 그룹을 포함시킬 순 없음
  - 하나의 사용자가 다수의 그룹에 속할 수도 있음
- IAM: Permission
  - 사용자 또는 그룹에게 정책, 또는 IAM이라고 불리는 JSON 문서를 지정할 수 있음
  - 이 정책들을 사용해 사용자들의 권한을 정의할 수 있게 됨
  - AWS에서는 모든 사용자에게 모든 권한을 허용하지 않음 => 보안 문제 및 비용 문제
  - 최소 권한의 원칙을 적용
    - 사용자가 꼭 필요로 하는 것 이상의 권한을 주지 않음



### IAM Policies

- IAM Pocicies Structure

  - 구성 요소

    - Version: 정책 언어 버전, 항상 '2012-10-17'이 포함
    - Id: 정책을 식별하는 ID (optional)
    - Statement: 한개 이상의 문장 (required)

  - Statement의 구성 요소

    - Sid: 문장 ID로 문장의 식별자 (optional)
    - Effect: 문장이 특정 API에 접근하는걸 허용할지 거부할지에 대한 내용 (Allow / Deny)
    - Principal: 특정 정책이 적용될 사용자, 계정, 혹은 역할로 구성
    - Action: effect에 기반해 허용 및 거부되는 API 호출의 목록
    - Resource: 적용될 action의 리소스 목록
    - Condition: statement가 언제 적용될지를 결정 (optional)

    ```json
    {
      "Version": "2012-10-17",
      "Id": "S3-Account-Permissions",
      "Statememt": [
        {
          "Sid": "1",
          "Effect": "Allow",
          "Pricipal": {
            "AWS": ["arn:aws:iam:123456789012:root"]
          },
          "Action": [
            "s3:GetObject",
            "s3:PutObject"
          ],
          "Resource": ["arn:aws:s3::mybucket/*"]
        }
      ]
    }
    ```



### IAM MFA

- Password Policy
  - Strong passwords = 계정의 보안을 높여줌
  - AWS password policy 세팅 방법
    - 비밀번호 최소 길이 설정
    - 특정 유형의 글자 사용 요구
    - IAM 사용자들의 비밀번호 변경 허용 및 금지
    - 일정 기간이 지나면 새 비밀번호 설정 요구
    - 사용자의 비밀번호 재사용을 막기
- MFA (Multi Factor Authentication)
  - 유저들은 AWS 계정에 접근할 수 있고 리소스들을 변경하고 삭제할 수도 있으므로 이 위험에서 계정을 보호해야함
  - MFA = password you know + security device you own
- AWS에서 MFA 장치 옵션
  - 가상 MFA 장치 (Virtual MFA device)
    - Google Authenticator (phone only)
    - Authy (multi- device)
    - 하나의 장치에서 여러 계정 및 사용자를 지원함
  - 범용 두 번째 인자 보안 키 (U2F - Universion 2nd Factor Security Key)
    - 물리적 장치
    - Yubico(AWS 제3자 회사) 의 YubiKey
    - 하나의 보안 키로 여러 루트 계정과 IAM 유저를 지원
  - 하드웨어 키 팝 MFA 장치 (Hardware Key Fob MFA Device)
    - 물리적 장치
    - Gemalto(AWS 제3자 회사)
  - 하드웨어 키 팝 MFA 장치 (미국 정부 AWS GovCloud 전용)
    - SurePassID(AWS 제3자 회사)



### AWS 엑세스 키, CLI 및 SDK

- 유저가 AWS에 접근하는 방법
  - AWS Management Console (protected by password + MFA)
  - AWS Command Line Interface (CLI): protected by access keys
  - AWS Software Developer Kit (SDK): for code -> protected by access keys
- 